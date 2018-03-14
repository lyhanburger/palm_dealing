import cv2
import numpy as np
def showall(img_name,center_points):
    IMAGE_USER = img_name.rstrip(".png").rstrip(".jpg").rstrip(".jpeg")
    img = cv2.imread(img_name)
    bg = img.copy()
    bg[:,:] = (0,0,0)
    rows, cols,_= img.shape
    trows = int(0.25*rows)
    tcols = int(0.25*cols)
    area_5678 = cv2.resize(img, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)
    bg[trows:3*trows,tcols:3*tcols] =  area_5678

    area_3 = cv2.imread("{0}_roi_7_out.jpg".format(IMAGE_USER))
    xrows, xcols,_ = area_3.shape
    area_3 = cv2.resize(area_3, None, fx = tcols/xcols, fy = trows/xrows, interpolation = cv2.INTER_CUBIC)
    bg[:trows,3*tcols:] = area_3
    print(center_points["roi_7"][0])
    start_point = (int(center_points["roi_7"][0]*2*tcols+tcols),int(center_points["roi_7"][1]*2*trows+trows))
    end_point = (int(0.875*cols),int(0.125*rows))
    cv2.line(bg,start_point, end_point,(0,255,0),15  )
    print("222")

#####
#0123
#4567
#89ab
#cdef
####
    
    cv2.imwrite("{0}_showall.jpg".format(IMAGE_USER),bg)
#if __name__ == "__main__":
#    center_points = roi("../image/yangxuanyue/yangxuanyue.jpg")
#    showall("../image/yangxuanyue/yangxuanyue.jpg", center_points)

