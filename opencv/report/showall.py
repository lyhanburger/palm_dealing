import cv2
import numpy as np
def showall(img_name,center_points):
    IMAGE_USER = img_name.rstrip(".png").rstrip(".jpg").rstrip(".jpeg")
    img = cv2.imread("{0}_contour_skin_roi.jpg".format(IMAGE_USER))
    bg = img.copy()
    bg[:,:] = (0,0,0)
    rows, cols,_= img.shape
    trows = int(0.25*rows)
    tcols = int(0.25*cols)

    area_5678 = cv2.resize(img, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)
    bg[trows:3*trows,tcols:3*tcols] =  area_5678

    area_3 = cv2.imread("{0}_feature_7_threshold_88.jpg".format(IMAGE_USER))
    xrows, xcols,_ = area_3.shape
    area_3 = cv2.resize(area_3, None, fx = tcols/xcols, fy = trows/xrows, interpolation = cv2.INTER_CUBIC)
    bg[:trows,3*tcols:] = area_3
    start_point = (int(center_points["roi_7"][0]*2*tcols+tcols),int(center_points["roi_7"][1]*2*trows+trows))
    end_point = (int(0.875*cols),int(0.125*rows))
    cv2.line(bg,start_point, end_point,(0,155,0),10  )
    cv2.putText(bg, "F7", (3*tcols,120), cv2.FONT_HERSHEY_SIMPLEX, 5, (0,0,255),20)


    area_12 = cv2.imread("{0}_feature_10_threshold_88.jpg".format(IMAGE_USER))
    xrows, xcols,_ = area_12.shape
    area_12 = cv2.resize(area_12, None, fx = 2*tcols/xcols, fy = trows/xrows, interpolation = cv2.INTER_CUBIC)
    bg[:trows,tcols:3*tcols] = area_12
    start_point = (int(center_points["roi_10"][0]*2*tcols+tcols),int(center_points["roi_10"][1]*2*trows+trows))
    end_point = (int((0.5)*cols),int((0.125)*rows))
    cv2.line(bg,start_point, end_point,(155,255,0),10  )
    cv2.putText(bg, "F10", (tcols,120), cv2.FONT_HERSHEY_SIMPLEX, 5, (0,0,255),20)

    area_de = cv2.imread("{0}_feature_9_threshold_88.jpg".format(IMAGE_USER))
    xrows, xcols,_ = area_de.shape
    area_de = cv2.resize(area_de, None, fx = 2*tcols/xcols, fy = trows/xrows, interpolation = cv2.INTER_CUBIC)
    bg[3*trows:,tcols:3*tcols] = area_de
    start_point = (int(center_points["roi_9"][0]*2*tcols+tcols),int(center_points["roi_9"][1]*2*trows+trows))
    end_point = (int((0.5)*cols),int((0.125+0.75)*rows))
    cv2.line(bg,start_point, end_point,(155,255,0),10  )
    cv2.putText(bg, "F9", (tcols,120+3*trows), cv2.FONT_HERSHEY_SIMPLEX, 5, (0,0,255),20)
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

