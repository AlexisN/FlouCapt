#!/bin/env python2
# -*- coding: utf-8 -*-


import sys, cv2
sys.path.append('..')
from PictureProcessing import *


if __name__ == "__main__":


    files = ["img/08-01-2014-13:34:58.jpg",
    "img/08-01-2014-13:35:29.jpg",
    "img/08-01-2014-13:36:36.jpg",
    "img/08-01-2014-13:36:50.jpg",
    "img/08-01-2014-13:37:16.jpg",
    "img/08-01-2014-13:40:30.jpg",
    "img/08-01-2014-13:43:04.jpg"]


    frontalface_alt = cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_alt.xml")
    frontalface_default = cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml")


    for fi in files:

        img = cv2.imread( fi )

        if img == None:
            print 'erreur image', fi
            continue


        grayimg = cv2.cvtColor(img, cv2.cv.CV_BGR2GRAY)
        grayimg = cv2.equalizeHist(grayimg)


        rects1 = frontalface_alt.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
        rects2 = frontalface_default.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))

        rectsG1 = frontalface_alt.detectMultiScale(grayimg, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
        rectsG2 = frontalface_default.detectMultiScale(grayimg, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))

        print "img  ", len(rects1) , "  ", len(rects2), fi
        print "gray ", len(rectsG1) , "  ", len(rectsG2), fi
        #print rectsG2
        print

        if len(rectsG2) > 0:
            rectsG2[:, 2:] += rectsG2[:, :2]
            final = PictureProcessing.smoothFaces(rectsG2, img)

            cv2.imwrite(fi+".png", final)







