import cv2
import numpy as np
def split():
    # 测试分离通道的效果
    img = cv2.imread(IMAGE_USER+"_roi_9_out.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #edges = cv2.Canny(gray, 3,60)
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    print(img.shape)
    print(ycrcb.shape)
    b,g,r = cv2.split(img)
    y,cr,cb = cv2.split(ycrcb)
    print(b.shape)
    cv2.imwrite("{0}_feature_9_b.jpg".format(IMAGE_USER), b)
    cv2.imwrite("{0}_feature_9_g.jpg".format(IMAGE_USER), g)
    cv2.imwrite("{0}_feature_9_r.jpg".format(IMAGE_USER), r)
    cv2.imwrite("{0}_feature_9_y.jpg".format(IMAGE_USER), y)
def test_blur():
    # 测试blur的参数
    image = cv2.imread(IMAGE_USER+"_roi_9_out.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #for i in range (1,25,2):
    #    # 从结果看， 9 比较合适
    #    blurred = cv2.blur(gray,(i,i))
    #    cv2.imwrite("{0}_feature_9_blur_{1}.jpg".format(IMAGE_USER, i ),blurred)
    blurred = cv2.blur(gray,(1,1))
    cv2.imwrite("{0}_feature_9_blur_{1}.jpg".format(IMAGE_USER, 1 ),blurred)

def test_threshold():
    # 测试二值化
    blurred = cv2.imread(IMAGE_USER+"_feature_9_blur_1.jpg")
#    for i in range(80,95,1):
#        ret,thresh1=cv2.threshold(blurred,i,255,cv2.THRESH_BINARY)
#        cv2.imwrite(IMAGE_USER+"_feature_9_threshold_{0}.jpg".format(i),thresh1)
    ret,thresh1=cv2.threshold(blurred,88,255,cv2.THRESH_BINARY)
    cv2.imwrite(IMAGE_USER+"_feature_9_threshold_{0}.jpg".format(88),thresh1)
def test_sobel():
    img = cv2.imread(IMAGE_USER+"_roi_9_out.jpg",0)
    x = cv2.Sobel(img,cv2.CV_16S,1,0)  
    y = cv2.Sobel(img,cv2.CV_16S,0,1)  
      
    absX = cv2.convertScaleAbs(x)   # 转回uint8  
    absY = cv2.convertScaleAbs(y)  
      
    dst = cv2.addWeighted(absX,8,absY,8,0)  
    cv2.imwrite("{0}_feature_9_soble.jpg".format(IMAGE_USER),dst)
def test_canny():
    gray = cv2.imread("../../image/yangxuanyue/yangxuanyue_roi_9_out.jpg",0)
    for i in range(1,30,1):
        for j in range(1,i,1):
            edges = cv2.Canny(gray, j, i)
            cv2.imwrite("{0}_feature_9_canny_{1}_{2}.jpg".format(IMAGE_USER, i,j),edges)
def test_dilate():
    kernel=np.uint8(np.zeros((5,5)))  
    for x in range(5):  
        kernel[x,2]=1;  
        kernel[2,x]=1;  
    img = cv2.imread("../../image/yangxuanyue/yangxuanyue_feature_9_threshold_88.jpg",0)
    dilated = cv2.dilate(img, kernel)
    cv2.imwrite("{0}_feature_9_dilate.jpg".format(IMAGE_USER),dilated)
def test_houghline():
#    img = cv2.imread("../../image/yangxuanyue/yangxuanyue_feature_9_threshold_88.jpg",0)
    img = cv2.imread("../../image/yangxuanyue/yangxuanyue_feature_9_dilate.jpg",0)
    edges = cv2.Canny(img, 10, 100)
    cv2.imwrite("{0}_feature_9_houghline_1.jpg".format(IMAGE_USER),edges)
    lines = cv2.HoughLines(edges,1,np.pi/180,11) 
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    lines1 = lines[:,0,:]
    i=0
    t_theta=0.17
    for rho,theta in lines1[:]: 
        i+=1
        if(theta>t_theta and theta<(3.14/2-t_theta)):continue
        if(abs(theta-0.0)<0.01):continue
        if(abs(theta-3.14/2)<0.001):continue
        if(theta>2.3):continue
        print(theta)

        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a)) 
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)
        if i>10:break;
    cv2.imwrite("{0}_feature_9_houghline.jpg".format(IMAGE_USER),img)
def feature_9(img_name):
    global IMAGE_FILE
    global IMAGE_USER
    IMAGE_FILE = img_name
    IMAGE_USER = img_name.replace(".jpg","").replace(".jpeg","").replace(".png","")
    print(IMAGE_USER)
    test_blur()
    test_threshold()
    #test_houghline()
    #test_dilate()
    return {"feature_9":True}
if __name__ == '__main__':
    feature_9("../../image/yangxuanyue/yangxuanyue.jpg")
