#!/bin/env python2

import cv2, time, os, sys

class PictureProcessing:


    @staticmethod
    def detectFaces( logger,  img ):
        """
        Detect a human faces in the picture
        """
        #cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt.xml")
        cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
        #cascade = cv2.CascadeClassifier("/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml")
        #cascade = cv2.CascadeClassifier("haarcascades/src/PictProcess/haarcascades/haarcascade_eye_tree_eyeglasses.xml")

        if cascade.empty() :
            logger.error( "The cascade classifier can't be loaded" )
            sys.exit(2)

        rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))

        if len(rects) == 0:
            return []
        rects[:, 2:] += rects[:, :2]
        return rects


    @staticmethod
    def smoothFaces(rects, img):
        """
        Apply a blur where human faces has been detected
        """
        for x1, y1, x2, y2 in rects:

            crop_img = img[y1:y2, x1:x2] # Crop from x1, y1 -> x2, y2
            crop_img = cv2.GaussianBlur(crop_img,(51,51),0)

            img[y1:y2, x1:x2] = crop_img

        return img

    @staticmethod
    def savePicture( logger, img ):
        """
        Save the picture passed in parameter
        """

        date = time.strftime('%Y-%m-%d', time.localtime())
        hour = time.strftime('%H:%M:%S', time.localtime())

        folder = "/var/floucapt/"+ date + "/"

        #if the folder doesn't exist
        if not os.path.isdir( folder ):
            os.makedirs( folder )


        file_name = date + "-" + hour + ".jpg"
        sucessSave = cv2.imwrite(folder + file_name, img)


        #--------------------------------------------------------------------
        # Temporary
        global oldPic
        try:
            oldPic
        except NameError:
            oldPic = ""
#        file = open("/var/www/FlouCapt2/picture.txt", "w")
        try:
            file = open("picture.txt", "w")
            file.write("Picture/"+ date + "/" + file_name + "\n")
            file.write(oldPic)
            file.close()
        except (RuntimeError, TypeError, NameError, IOError):
            pass

        oldPic = "Picture/"+ date + "/" + file_name
        #--------------------------------------------------------------------


        #if the picture recording failed
        if not sucessSave:
            logger.error("The picture could not be saved here : "+ folder+file_name )
        else:
            logger.info( "Picture has been saved at "+date + "-"+ hour "   in file : " + folder+file_name )

