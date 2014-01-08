#!/usr/bin/python2

import cv2

class Camera:


    @staticmethod
    def getPicture():

        vc = cv2.VideoCapture("http://192.168.1.26/videostream.cgi?user=admin&pwd=&.mjpg")
        #vc = cv2.VideoCapture(0)



        if vc.isOpened(): # try to get the first frame
            rval, img = vc.read()
        else:
            rval = False
            img = None

        return rval, img;
