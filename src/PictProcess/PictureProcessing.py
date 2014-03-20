#!/bin/env python2

import cv2, time, os, sys

class PictureProcessing:


    @staticmethod
    def detectFaces( img ):
        """
        Detect a human faces in the picture
        """
        #cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt.xml")
        cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
        #cascade = cv2.CascadeClassifier("haarcascades/src/PictProcess/haarcascades/haarcascade_eye_tree_eyeglasses.xml")

        if cascade.empty() :
            print "The cascade classifier can't be loaded"
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
    def savePicture( img ):
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


#        file = open("/var/www/FlouCapt2/picture.txt", "w")
#        file.write("/var/floucapt/"+ date + "/" + file_name)
#        file.close()


        #if the picture recording failed
        if not sucessSave:
            print "The picture could not be saved here : "+ folder+file_name
        else:
            print "Picture has been saved at "+date + "-"+ hour

