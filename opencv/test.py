from feature.seven.feature_7 import feature_7
from feature.nine.feature_9 import feature_9
from feature.ten.feature_10 import feature_10
from cutout.cutout import cutout
from roi.roi import roi
from report.showall import showall
from report.report import report 
def test1():
    res = feature_7("image/yangxuanyue/yangxuanyue.jpg")
def test2():
    IMAGE_NAME = "image/yangxuanyue/yangxuanyue.jpg"
    cutout(IMAGE_NAME)
    center_points = roi(IMAGE_NAME)
    report_list = {}
    report_list.update(feature_7(IMAGE_NAME))
    report_list.update(feature_9(IMAGE_NAME))
    report_list.update(feature_10(IMAGE_NAME))
    print(center_points)
    showall(IMAGE_NAME, center_points)
    report(IMAGE_NAME, report_list)


test2()


