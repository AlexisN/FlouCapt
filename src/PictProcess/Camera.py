#!/usr/bin/python2

import cv2

class Camera:


    @staticmethod
    def getPicture():
        #vc = cv2.VideoCapture("http://192.168.0.9/videostream.asf?user=guest&pwd=guest")
        vc = cv2.VideoCapture(0)

        if vc.isOpened(): # try to get the first frame
            rval, img = vc.read()
        else:
            rval = False

        return rval, img;
