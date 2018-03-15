## 重点
* 所有的文件图片存放在image中

## 模块说明

#### cutout

```shell
  
python3 cutout.py ../image/name/name.jpg

```
* output
  * ../imgae/name/name_skin.jpg #除去背景的图片
  * ../image/name/name_contour.jpg #轮廓

#### roi

```shell
python3 roi.py ../image/name/name.jpg
```
* output
  * ../image/name/name_roi_main.jpg #skin上在手掌上画个框
  * ../image/name/name_roi_main_output.jpg #框里面的内容
  * ../image/name/name_roi_7/8/9/10.jpg
