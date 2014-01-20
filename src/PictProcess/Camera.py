#!/bin/env python2

import cv2


class Camera:
    """This class allows to get a picture from a webcam/ipwebcam"""

    @staticmethod
    def getPicture( link ):
        """return a picture from a stream of an webcam/ipwebcam
        """

        #
        try:
            var = int(link)
        except ValueError:
            var = link

        vc = cv2.VideoCapture( var )



        if vc.isOpened(): # try to get the first frame
            rval, img = vc.read()
        else:
            rval = False
            img = None

        return rval, img;
