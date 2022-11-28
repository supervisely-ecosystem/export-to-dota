
<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/115161827/203993840-5a170216-d7a2-4e45-a74a-4b4c856e5b2f.jpg"/>  

# Export to DOTA

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-to-use">How To Use</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/export-to-dota)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/export-to-dota)
[![views](https://app.supervise.ly/img/badges/views/supervisely-ecosystem/export-to-dota.png)](https://supervise.ly)
[![runs](https://app.supervise.ly/img/badges/runs/supervisely-ecosystem/export-to-dota.png)](https://supervise.ly)

</div>

# Overview

Converts project in [Supervisely](https://docs.supervise.ly/data-organization/00_ann_format_navi) format to [DOTA](https://captain-whu.github.io/DOTA/dataset.html) and prepares downloadable archive. 

DOTA is [one of the formats](https://github.com/open-mmlab/mmrotate/tree/main/tools/data#data-preparation-for-rotation-detection) supported by [mmrotate](https://github.com/open-mmlab/mmrotate) ![GitHub Org's stars](https://img.shields.io/github/stars/open-mmlab/mmrotate?style=social)


## Preparation

Project object classes shapes must be: `Polygon`, `Bitmap`, `Line`, `Rectangle` or `Any Shape` with any of the mentioned shapes, all other shapes will be ignored, and will not be presenting in resulted project. You can convert object classes shapes using [convert-class-shape](https://ecosystem.supervise.ly/apps/convert-class-shape) application.

## Output archive structure

```
archive.tar
├── dataset_name_1
│   ├── images
│   └── labelTxt
└── dataset_name_2
    ├── images
    └── labelTxt
```

## Output annotation format

**IMAGE_001.txt**

First 2 lines of the annotaion is image metadata.

Other lines in the annotation file are labels: `x1`, `y1`, `x2`, `y2`, `x3`, `y3`, `x4`, `y4`, `label_name` `complexity` 

```
imagesource:imagesource
gsd:None
388.0 1190.0 473.0 1144.0 488.0 1171.0 403.0 1217.0 truck 0
575.0 1024.0 591.0 995.0 696.0 1053.0 679.0 1082.0 truck 0
709.0 1047.0 753.0 1045.0 754.0 1063.0 710.0 1065.0 car 0
714.0 1005.0 714.0 980.0 764.0 980.0 764.0 1005.0 car 0
710.0 923.0 752.0 923.0 752.0 942.0 710.0 942.0 car 0
1125.0 933.0 1171.0 919.0 1176.0 936.0 1130.0 950.0 car 0
380.0 1475.0 519.0 1351.0 541.0 1376.0 402.0 1499.0 truck 0
```

# How to use

App can be launched from ecosystem, images project or images dataset

## Run from Ecosystem

**Step 1.** Run the app from Ecosystem

<img src="https://user-images.githubusercontent.com/115161827/203999489-57154128-ae87-4813-a2c8-560ce6614ed4.jpg" width="80%" style='padding-top: 10px'>  

**Step 2.** Select input project or dataset and press the Run button

<img src="https://user-images.githubusercontent.com/115161827/203999453-a36b56c9-5be5-475f-b075-3f02461c7503.gif" width="80%" style='padding-top: 10px'>

## Run from Images Project or Dataset

**Step 1.** Run the application from the context menu of the Images Project or Dataset

<img src="https://user-images.githubusercontent.com/115161827/203999520-b935e4a5-f06f-4e87-afef-09fb82026a9e.png" width="80%" style='padding-top: 10px'>  

**Step 2.** Press the Run button

<img src="https://user-images.githubusercontent.com/115161827/203999543-d85c56bb-de1b-4ec2-a00a-6ecc95d3f408.png" width="80%" style='padding-top: 10px'>

## Result

<img src="https://user-images.githubusercontent.com/115161827/203999558-b427801a-8e84-4064-a6a9-0925e4dd6c58.jpg" width="80%" style='padding-top: 10px'>
