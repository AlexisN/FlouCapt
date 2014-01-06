#!/usr/bin/python2

import time
import cv2
import sys
from cv2.cv import *

class PictureProcessing:


    @staticmethod
    def detect( img ):
        #cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt.xml")
        cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

        rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))

        if len(rects) == 0:
            return []
        rects[:, 2:] += rects[:, :2]
        return rects


    @staticmethod
    def box(rects, img):

        for x1, y1, x2, y2 in rects:
            #center = ((x2+x1)/2,(y1+y2)/2)
            #axes = ((x2-x1)/2, (y2-y1)/2)
            #cv2.ellipse(img, center, axes, 0, 360 , 0,(127, 255, 0), 2)

            crop_img = img[x1:x2, y1:y2] # Crop from x1, y1 -> x2, y2
            blur = cv2.GaussianBlur(crop_img,(51,51),0)
            img[x1:x2, y1:y2] = blur


        date = time.strftime('%d-%m-%y %H:%M',time.localtime())
        file_name = date + ".png"
        cv2.imwrite(file_name, img)
