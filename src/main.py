import os

import supervisely as sly
from supervisely.io.fs import get_file_name, mkdir

from src.functions import (
    convert_obj_classes_to_poly,
    convert_sly_to_dota,
    get_anns_list,
    upload_project_to_tf,
)
from src.globals import DATASET_ID, PROJECT_DIR, PROJECT_ID, api
import src.workflow as w

@sly.handle_exceptions(has_ui=False)
def main():
    project = api.project.get_info_by_id(id=PROJECT_ID)
    project_meta = sly.ProjectMeta.from_json(data=api.project.get_meta(id=PROJECT_ID))
    project_meta = convert_obj_classes_to_poly(project_meta=project_meta)

    if DATASET_ID is not None:
        datasets = [api.dataset.get_info_by_id(id=DATASET_ID)]
        w.workflow_input(api, DATASET_ID, type="dataset")
    else:
        datasets = api.dataset.get_list(project_id=PROJECT_ID)
        w.workflow_input(api, PROJECT_ID, type="project")
    progress_ds = sly.Progress(message="Exporting datasets", total_cnt=len(datasets))
    for dataset in datasets:
        dataset_dir = os.path.join(PROJECT_DIR, dataset.name)
        images_dir = os.path.join(dataset_dir, "images")
        ann_dir = os.path.join(dataset_dir, "labelTxt")
        mkdir(images_dir)
        mkdir(ann_dir)
        images_infos = api.image.get_list(dataset_id=dataset.id)
        images_ids = [img_info.id for img_info in images_infos]
        images_paths = [
            os.path.join(images_dir, img_info.name) for img_info in images_infos
        ]
        anns = get_anns_list(api=api, ds_id=dataset.id, project_meta=project_meta)
        anns_paths = [
            os.path.join(ann_dir, f"{get_file_name(img_info.name)}.txt")
            for img_info in images_infos
        ]

        progress_img = sly.Progress(message="Processing images", total_cnt=len(images_ids))
        for batch_img_ids, batch_img_paths, batch_anns, batch_anns_paths in zip(
            sly.batched(images_ids),
            sly.batched(images_paths),
            sly.batched(anns),
            sly.batched(anns_paths),
        ):
            convert_sly_to_dota(
                anns_paths=batch_anns_paths,
                anns=batch_anns,
                project_meta=project_meta,
            )
            api.image.download_paths(
                dataset_id=dataset.id, ids=batch_img_ids, paths=batch_img_paths
            )
            progress_img.iters_done_report(len(batch_img_ids))
        progress_ds.iter_done_report()

    file_info = upload_project_to_tf(api, project)
    w.workflow_output(api, file_info)

if __name__ == "__main__":
    sly.main_wrapper("main", main)