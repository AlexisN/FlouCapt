#!/bin/env python2

import cv2


class Camera:
    """Class that allow obtain a picture since a image source (webcam or ip camera)"""

    @staticmethod
    def getPicture( link ):
        """Return a picture since a webcam or an ip camera
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
