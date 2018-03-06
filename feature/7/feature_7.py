import cv2
import argparse  
import numpy as np
parser = argparse.ArgumentParser()  
parser.add_argument("image", help="input image name")  
args = parser.parse_args() 
IMAGE_FILE = args.image
IMAGE_USER = IMAGE_FILE.rstrip(".jpg")
print(IMAGE_USER)
def split():
    # 测试分离通道的效果
    img = cv2.imread(IMAGE_USER+"_roi_7_out.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #edges = cv2.Canny(gray, 3,60)
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    print(img.shape)
    print(ycrcb.shape)
    b,g,r = cv2.split(img)
    y,cr,cb = cv2.split(ycrcb)
    print(b.shape)
    cv2.imwrite("{0}_feature_7_b.jpg".format(IMAGE_USER), b)
    cv2.imwrite("{0}_feature_7_g.jpg".format(IMAGE_USER), g)
    cv2.imwrite("{0}_feature_7_r.jpg".format(IMAGE_USER), r)
    cv2.imwrite("{0}_feature_7_y.jpg".format(IMAGE_USER), y)
def test_blur():
    # 测试blur的参数
    image = cv2.imread(IMAGE_USER+"_roi_7_out.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for i in range (1,25,2):
        # 从结果看， 9 比较合适
        blurred = cv2.blur(gray,(i,i))
        cv2.imwrite("{0}_feature_7_blur_{1}.jpg".format(IMAGE_USER, i ),blurred)
def test_threshold():
    # 测试二值化
    blurred = cv2.imread(IMAGE_USER+"_feature_7_blur_1.jpg")
    for i in range(80,95,1):
        ret,thresh1=cv2.threshold(blurred,i,255,cv2.THRESH_BINARY)
        cv2.imwrite(IMAGE_USER+"_feature_7_threshold_{0}.jpg".format(i),thresh1)
test_threshold()

        

