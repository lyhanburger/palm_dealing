from feature.seven.feature_7 import feature_7
from roi.roi import roi
from report.showall import showall
def test1():
    res = feature_7("image/yangxuanyue/yangxuanyue.jpg")
def test2():
    center_points = roi("image/yangxuanyue/yangxuanyue.jpg")
    print(center_points)
    showall("image/yangxuanyue/yangxuanyue.jpg", center_points)

test2()


