import os
from typing import List

import cv2
import numpy as np
import supervisely as sly

from src.globals import (
    PROJECT_DIR,
    STORAGE_DIR,
    SUPPORTED_GEOMETRY_TYPES,
    TASK_ID,
    TEAM_ID,
)


def convert_obj_classes_to_poly(project_meta: sly.ProjectMeta):
    ro_bbox_obj_classes = [
        sly.ObjClass(
            name=f"ro_bbox_{obj_class.name}",
            geometry_type=sly.Polygon,
            color=obj_class.color,
        )
        for obj_class in project_meta.obj_classes
        if obj_class.geometry_type in SUPPORTED_GEOMETRY_TYPES
    ]
    project_meta = project_meta.add_obj_classes(new_obj_classes=ro_bbox_obj_classes)
    return project_meta


def get_anns_list(api: sly.Api, ds_id: int, project_meta: sly.ProjectMeta):
    ann_infos = api.annotation.get_list(dataset_id=ds_id)
    ann_jsons = [ann_info.annotation for ann_info in ann_infos]
    anns = [
        sly.Annotation.from_json(data=ann_json, project_meta=project_meta)
        for ann_json in ann_jsons
    ]
    return anns


def convert_sly_to_dota(
    anns_paths: List[str], anns: List[sly.Annotation], project_meta: sly.ProjectMeta
):
    for ann, ann_path in zip(anns, anns_paths):
        file = open(ann_path, "w")
        file.write("imagesource:imagesource\ngsd:None\n")
        for label in ann.labels:
            if type(label.geometry) not in SUPPORTED_GEOMETRY_TYPES:
                continue
            ro_bbox_line = label_to_ro_bbox(label=label, project_meta=project_meta)
            file.write(f"{ro_bbox_line}\n")


def label_to_ro_bbox(label: sly.Label, project_meta: sly.ProjectMeta):
    orig_label_name = label.obj_class.name
    ro_bbox_obj_class_name = f"ro_bbox_{label.obj_class.name}"
    ro_bbox_obj_class = project_meta.get_obj_class(ro_bbox_obj_class_name)

    if type(label.geometry) != sly.Polygon:
        new_geometry = label.geometry.convert(new_geometry=sly.Polygon)[0]
        label = sly.Label(geometry=new_geometry, obj_class=ro_bbox_obj_class)

    poly_ext = label.geometry.exterior
    points = []
    for coord in poly_ext:
        coords = np.array([coord.col, coord.row])
        points.append(coords)
    points = np.array(points)

    rect = cv2.minAreaRect(points)
    box = cv2.boxPoints(rect)
    rot_box = np.int0(box)

    coords = [[coord[1], coord[0]] for coord in rot_box]
    x1, y1, x2, y2, x3, y3, x4, y4 = (
        float(coords[0][1]),
        float(coords[0][0]),
        float(coords[1][1]),
        float(coords[1][0]),
        float(coords[2][1]),
        float(coords[2][0]),
        float(coords[3][1]),
        float(coords[3][0]),
    )

    ann_line = f"{x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4} {orig_label_name} 0"
    return ann_line


def upload_project_to_tf(api: sly.Api, project: sly.ProjectInfo) -> sly.api.file_api.FileInfo:
    full_archive_name = f"{str(project.id)}_{project.name}.tar"
    result_archive = os.path.join(STORAGE_DIR, full_archive_name)
    sly.fs.archive_directory(PROJECT_DIR, result_archive)
    sly.logger.info("Result directory is archived")
    upload_progress = []
    remote_archive_path = os.path.join(
        sly.team_files.RECOMMENDED_EXPORT_PATH, f"export-to-dota/{TASK_ID}_{full_archive_name}")

    def _print_progress(monitor, upload_progress):
        if len(upload_progress) == 0:
            upload_progress.append(
                sly.Progress(
                    message="Upload {!r}".format(full_archive_name),
                    total_cnt=monitor.len,
                    ext_logger=sly.logger,
                    is_size=True,
                )
            )
        upload_progress[0].set_current_value(monitor.bytes_read)

    file_info = api.file.upload(
        TEAM_ID,
        result_archive,
        remote_archive_path,
        lambda m: _print_progress(m, upload_progress),
    )
    sly.logger.info(f"Uploaded to Team-Files: '{file_info.storage_path}'")
    api.task.set_output_archive(
        TASK_ID, file_info.id, full_archive_name, file_url=file_info.storage_path
    )
    return file_info
