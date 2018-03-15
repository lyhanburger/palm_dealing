import cv2
import numpy as np

def calK(p0,p1):
    if p0[0] == p1[0]:
        print("equal")
        return 100 
    if abs(p0[1] - p1[1])<20:
        return 0
    k = (p1[1]-p0[1])/(p1[0]-p0[0])
    return k
def roi_main(img,points):
    img = img.copy()
    top_left=(points[0][0],points[4][1])
    bottom_right = (points[7][0]+(points[6][0]-points[5][0]), int(points[0][1]-(points[5][1]-points[0][1])*1.2))
    center_points.update({"roi_main":((top_left[0]+bottom_right[0])/2/img_cols,(top_left[1]+bottom_right[1])/2/img_rows)})
    cv2.rectangle(img,top_left, bottom_right,(255,255,0),3)
    cv2.rectangle(contour_skin,top_left, bottom_right,(255,255,0),8)
    cv2.imwrite("{0}_roi_main.jpg".format(IMAGE_USER),img)
    out = img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0],:]
    cv2.imwrite("{0}_roi_main_out.jpg".format(IMAGE_USER),out)
def roi_10(img, p):
    img = img.copy()
    top_left=(p[2][0],p[2*2+0][1])
    bottom_right = (p[2*2+1][0],int((p[0*2+0][1]+p[2*2+1][1])/2))
    center_points.update({"roi_10":((top_left[0]+bottom_right[0])/2/img_cols,(top_left[1]+bottom_right[1])/2/img_rows)})
    cv2.rectangle(img,top_left, bottom_right,(255,155,0),8)
    cv2.rectangle(contour_skin,top_left, bottom_right,(255,155,0),8)
    cv2.imwrite("{0}_roi_10.jpg".format(IMAGE_USER),img)
    out = img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0],:]
    cv2.imwrite("{0}_roi_10_out.jpg".format(IMAGE_USER),out)
    
def roi_9(img, p):
    img = img.copy()
    top_left=(p[2][0],p[2*2+0][1])
    bottom_right = (p[3*2+1][0],int(p[0*2+0][1]+(-p[0*2+0][1]+p[2*2+1][1])*0.3))
    center_points.update({"roi_9":((top_left[0]+bottom_right[0])/2/img_cols,(top_left[1]+bottom_right[1])/2/img_rows)})
    cv2.rectangle(img,top_left, bottom_right,(255,55,55),3)
    cv2.rectangle(contour_skin,top_left, bottom_right,(255,55,55),8)
    cv2.imwrite("{0}_roi_9.jpg".format(IMAGE_USER),img)
    out = img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0],:]
    cv2.imwrite("{0}_roi_9_out.jpg".format(IMAGE_USER),out)
def roi_7(img, p):
    img = img.copy()
    top_left=(p[2*2+1][0],p[3*2+0][1])
    bottom_right = (p[3*2+0][0],p[0*2+0][1])
    center_points.update({"roi_7":((top_left[0]+bottom_right[0])/2/img_cols,(top_left[1]+bottom_right[1])/2/img_rows)})
    cv2.rectangle(img,top_left, bottom_right,(0,55,255),3)
    cv2.rectangle(contour_skin,top_left, bottom_right,(0,55,255),8)
    cv2.imwrite("{0}_roi_7.jpg".format(IMAGE_USER),img)
    out = img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0],:]
    cv2.imwrite("{0}_roi_7_out.jpg".format(IMAGE_USER),out)
def roi(img_file):
    global IMAGE_FILE
    global IMAGE_USER
    global center_points
    global img_rows
    global img_cols
    global contour_skin
    center_points = {}
    IMAGE_FILE = img_file
    IMAGE_USER = IMAGE_FILE.replace(".jpg","").replace(".jpeg","").replace(".png","")
    img = cv2.imread('{0}_contour.jpg'.format(IMAGE_USER))
    contour_skin = cv2.imread('{0}_contour_skin.jpg'.format(IMAGE_USER))
    img_rows, img_cols, _ = img.shape
    src = cv2.imread('{0}_skin.jpg'.format(IMAGE_USER))
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 127, 255,0)
    imt,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    hull = cv2.convexHull(cnt,returnPoints = False)  ###返回凸包的点的坐标，returnPoints = False时反馈的坐标点在轮廓描述集合中点的编号，
    defects = cv2.convexityDefects(cnt,hull) ##反馈的是Nx4的数组，第一列表示的是起点（轮廓集合中点的编号）、第二列表示的是终点（轮廓集合中点的编号）
    ##第三列表示的是最远点（轮廓集合中点的编号），第四列表示的是最远点到凸轮廓的最短距离
    defects = defects[:,0,:]
    temp=sorted(defects,key=lambda entity:entity[3],reverse=True)
    points = []
    for i in range(4):
        s,e,f,d = temp[i]
        far = tuple(cnt[f][0])
        number = f
        while calK(cnt[number-1,0],cnt[number,0])<1:
            number-=3
        right = number
        number = f
        while calK(cnt[number,0],cnt[number+1,0])<1:
            number+=3
        left = number
        points.append(tuple(cnt[left,0]))
        points.append(tuple(cnt[right,0]))
        cv2.circle(img,far,14,[0,0,255],-1)
        cv2.circle(img,tuple(cnt[left][0]),14,[255,255,255],-1)
        cv2.circle(img,tuple(cnt[right][0]),14,[0,255,255],-1)
    points = sorted(points, key=lambda x:x[0])
    #roi_main(img,points)
    #roi_10(img,points)
    #roi_9(img,points)
    #roi_7(img,points)
    roi_main(src,points)
    roi_10(src,points)
    roi_9(src,points)
    roi_7(src,points)
    cv2.imwrite("{0}_contour_skin_roi.jpg".format(IMAGE_USER),contour_skin )
    return center_points
if __name__ == "__main__":    
    print(roi("../image/yangxuanyue/yangxuanyue.jpg"))
