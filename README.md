
<div align="center" markdown>
<img src="https://user-images.githubusercontent.com/115161827/203993840-5a170216-d7a2-4e45-a74a-4b4c856e5b2f.jpg"/>  

# Export to DOTA

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-to-use">How To Use</a>
</p>

</div>

# Overview

Converts [Supervisely](https://docs.supervise.ly/data-organization/00_ann_format_navi) format project to [DOTA](https://captain-whu.github.io/DOTA/dataset.html) and prepares downloadable archive.

## Preparation

Project object classes shapes must be: `Polygon`, `Bitmap`, `Line`, `Rectangle` or `Any Shape` with any of the mentioned shapes, all other shapes will be skipped. You can convert object classes shapes using [convert-class-shape](https://ecosystem.supervise.ly/apps/convert-class-shape) application.

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

<img src="https://user-images.githubusercontent.com/115161827/203979491-9bd59979-e8c9-4803-920d-d61460ed2080.jpg" width="80%" style='padding-top: 10px'>  

**Step 2.** Select input project or dataset and press the Run button

<img src="https://user-images.githubusercontent.com/115161827/203979469-e8946f07-b659-47b0-8932-ddb44fb29bba.gif" width="80%" style='padding-top: 10px'>

## Run from Images Project or Dataset

**Step 1.** Run the application from the context menu of the Images Project or Dataset

<img src="https://user-images.githubusercontent.com/115161827/203980155-b7bcc1fe-1391-4fdb-a351-ad41e1611627.png" width="80%" style='padding-top: 10px'>  

**Step 2.** Press the Run button

<img src="https://user-images.githubusercontent.com/115161827/203980165-aa9d0f66-a26c-4293-8caa-8f31710f3f42.png" width="80%" style='padding-top: 10px'>

## Result

<img src="https://user-images.githubusercontent.com/115161827/203984216-7306f3f0-4702-492d-876f-1aee053f62e2.jpg" width="80%" style='padding-top: 10px'>
