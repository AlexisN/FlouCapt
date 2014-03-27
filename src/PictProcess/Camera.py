#!/bin/env python2
# -*-coding:UTF-8 -*

import cv2, time


class Camera:
    """This class allows to get a picture from a webcam/ipwebcam"""

    @staticmethod
    def getPicture( logger, link ):
        """return a picture from a stream of an webcam/ipwebcam
        """

        # Determine if the link is a integer or a string
        try:
            var = int(link)
        except ValueError:
            var = link


        vc = cv2.VideoCapture( var )

        time.sleep(4)


        if not vc.isOpened():
            logger.error("Unable to contact the camera")
            raise Exception(2)


        # try to get the first frame
        rval, img = vc.read()
        if rval == False:
            logger.error("Unable to contact the camera")
            raise Exception(2)
        if img == None:
            logger.error("The picture retrieve by the camera is not valid")
            raise Exception(1)





#       exception = 1  : The picture retrieve by the camera is not valid
#       exception = 2  : unable to contact the camera
        return img;
