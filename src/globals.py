import os
from distutils.util import strtobool

import supervisely as sly
from dotenv import load_dotenv
from supervisely.io.fs import mkdir

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api.from_env()

TEAM_ID = sly.env.team_id()
WORKSPACE_ID = sly.env.workspace_id()
PROJECT_ID = sly.env.project_id()
DATASET_ID = sly.env.dataset_id(raise_not_found=False)

SUPPORTED_GEOMETRY_TYPES = [
    sly.AnyGeometry,
    sly.Bitmap,
    sly.Polygon,
    sly.Polyline,
    sly.Rectangle,
]

app = sly.Application()

STORAGE_DIR = sly.app.get_data_dir()
PROJECT_DIR = os.path.join(STORAGE_DIR, "DOTA")
mkdir(PROJECT_DIR, True)
