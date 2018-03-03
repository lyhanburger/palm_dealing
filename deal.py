import cv2
import os
from scipy.misc import *
import numpy as np
import matplotlib.pyplot as plt


class Predeal:

    def preALLDeal(self,path):
        # 00 open a picture
        img = self.open(path)

        # get height and width of original picture
        h, w = img.shape[:2]

        # 01 turn rgb to ycrcb
        imgYCC = self.imgYCC(img)

        # 02 blured
        # you can choose tmp parameters
        tmp = (3, 3)
        # choice = 0 no blure choice = 1 blure choice = 2 filter2D choice = 3 Gaussian
        blured_img = self.blured(1, imgYCC , tmp)

        # 03 treshing
        tresh_img = self.thresh(blured_img)


        # 04 get contours
        contours = self.contours(tresh_img)

        # 05 find_min_rec
        self.find_min_rec(img, contours)
        # draw images
        # opencv的一个像素为：[B,G,R] ,matplotlib的一个像素为：[R,G,B]
        plt.figure()
        img_ = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.subplot(221), plt.imshow(img_), plt.title('original'), plt.axis('off')

        #blureImg_ = cv2.cvtColor(blured_img, cv2.COLOR_BGR2RGB)
        plt.subplot(222), plt.imshow(blured_img), plt.title('blured'), plt.axis('off')

        plt.subplot(223), plt.imshow(tresh_img, cmap='gray'), plt.title('otsu treshing'), plt.axis('off')

        cv2.drawContours(img_, contours, -1, (0, 0, 255), 3)
        plt.subplot(224),plt.imshow(img_), plt.title('contours'), plt.axis('off')

        plt.show()



    def open(self, path):
        if os.path.exists(path) and os.path.isfile(path):
            return cv2.imread( path )
        else:
            print("no exists file = ", path)
            return None

    def imgYCC(self,img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

    def thresh(self, img):
        if img.all() == None:
            print('please open an image first')
            return None

        img_gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)
        #  gray_img
        #  plt.hist(img_gray.ravel(), 256)
        #  plt.show()
        retval, im_at_fixed = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        return im_at_fixed

    def blured(self, choice, img, tmp):
        if choice == 0:
            return img
        elif choice == 1:
            return cv2.blur(img, tmp)
        elif choice == 2:
            kernel = np.ones(tmp, np.float32) / (tmp[0]*tmp[1])
            return cv2.filter2D(img, -1, kernel)
        elif choice == 3:
            return cv2.GaussianBlur(img, tmp, 0)
        elif choice == 4:
            kernel = np.ones(tmp, np.float32)


    def contours(self, img):
        if img.all() == None:
            print('please open an image first')
            return None

        image, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def find_min_rec(self, img, contours):
        for p in contours:
            x, y, w, h = cv2.boundingRect(p)
            cv2.rectangle(img, (x, y), (x+w , y+h), (0, 255, 0), 2)
            # find minimum area
            rect = cv2.minAreaRect(p)
            # calculate coordinates of the minimum area rectangle
            box = cv2.boxPoints(rect)
            # normalize coordinates to integers
            box = np.int0(box)
            # draw contours
            cv2.drawContours(img, [box], 0, (0, 0, 255), 3)

            # calculate center and radius of minimum enclosing circle
            (x, y), radius = cv2.minEnclosingCircle(p)
            # cast to integers
            center = (int(x), int(y))
            radius = int(radius)
            # draw the circle
            img = cv2.circle(img, center, radius, (0, 255, 0), 2)

        cv2.drawContours(img, contours, -1, (255, 0, 0), 1)


if __name__ == '__main__':
    IMGPATH = '/Users/liyuhan/Downloads/PalmPrint_DB/img/IMG_001 (1).JPG'
    # IMGPATH ='/Users/liyuhan/Desktop/1.jpg'
    t = Predeal()
    t.preALLDeal(IMGPATH)
