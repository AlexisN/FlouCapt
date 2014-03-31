#!/bin/env python2
# -*-coding:UTF-8 -*

import cv2, time


class Camera:
    """This class allows to get a picture from a webcam/ipwebcam"""

    @staticmethod
    def getPicture( logger, link ):
        """
        :param logger: Logger to write message
        return a picture from a stream of an webcam/ipwebcam
        raise exception if It's unable to contact the camera
        """

        # Determine if the link is a integer or a string
        # Indeed, VideoCapture method should receive as parameter :
        #   An integer to a device ( for a webcam ...)
        #   A string to a web url of video stream of camera
        try:
            var = int(link)
        except ValueError:
            var = link


        # Contact the camera
        try:
            vc = cv2.VideoCapture( var )
        except:
            logger.error("Unable to contact the camera")
            raise Exception(2)

        # For technical reason, the program must wait a moment
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

        return img;
