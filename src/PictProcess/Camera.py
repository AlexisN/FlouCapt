#!/bin/env python2

import cv2


class Camera:
    """This class allows to get a picture from a webcam/ipwebcam"""

    @staticmethod
    def getPicture( logger, link ):
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
            if rval == False or img == None:
                value = 1
                logger.error("The picture retrieve by the camera is not valid")
            else:
                value = 0
        else:
            value = 2
            logger.error("unable to contact the camera")
            img = None



#       value = 0  : Ok
#       value = 1  : The picture retrieve by the camera is not valid
#       value = 2  : unable to contact the camera
        return value, img;
