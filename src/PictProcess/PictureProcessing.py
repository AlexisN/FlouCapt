#!/bin/env python2
# -*-coding:UTF-8 -*

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
            raise Exception(3)

        # Detection faces on a gray image
        grayimg = cv2.cvtColor(img, cv2.cv.CV_BGR2GRAY)
        grayimg = cv2.equalizeHist(grayimg)

        rects = cascade.detectMultiScale(grayimg, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))

        if len(rects) == 0:
            return []
        rects[:, 2:] += rects[:, :2]

#        rects[:, 0] -= ((rects[:, 2] - rects[:, 0] ) /5) #x1
#        rects[:, 2] += ((rects[:, 2] - rects[:, 0] ) /5) #x2
#        rects[:, 3] -= ((rects[:, 1] - rects[:, 3] ) /5) #y1
#        rects[:, 1] += ((rects[:, 1] - rects[:, 3] ) /5) #y2



#       exception 3  : The cascade classifier can't be loaded
        return rects


    @staticmethod
    def smoothFaces(rects, img):
        """
        Apply a blur where human faces has been detected
        """
        for x1, y1, x2, y2 in rects:

            blur = img[y1:y2, x1:x2] # Crop from x1, y1 -> x2, y2
            blur = cv2.GaussianBlur(blur,(151,151),0)

            # I want to put logo on top-left corner, So I create a ROI
            roi = img[y1:y2, x1:x2 ]

            # Now create a mask of logo and create its inverse mask also
            width, height, h = blur.shape
            center = (width/2, height/2)
            img2gray = blur.copy()

            cv2.rectangle(img2gray, (0,0), (width,height), (0, 0, 0), -1)
            cv2.ellipse(img2gray, center, center, 0, 360 , 0,(255, 255, 255), -1)

            img2gray = cv2.cvtColor(img2gray,cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(img2gray, 0, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)

            # Now black-out the area of logo in ROI
            img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

            # Take only region of logo from logo image.
            img2_fg = cv2.bitwise_and(blur,blur,mask = mask)


            # Put logo in ROI and modify the main image
            dst = cv2.add(img1_bg,img2_fg)
            img[y1:y2, x1:x2 ] = dst

        return img

    @staticmethod
    def savePicture( logger, floucaptFolder, img ):
        """
        Save the picture passed in parameter
        """

        date = time.strftime('%Y-%m-%d', time.localtime())
        hour = time.strftime('%H:%M:%S', time.localtime())

#        folder = "/var/www/FlouCapt2/Picture/"+ date + "/"
#        folder = "out/"+ date + "/"
        folder = floucaptFolder + "/pictures/"+ date + "/"

        #if the folder doesn't exist
        if not os.path.isdir( folder ):
            try:
                os.makedirs( folder )
            except:
                logger.error("The folder '"+ folder + "' doesn't exist and could not be created")
                raise Exception(4)


        file_name = date + "-" + hour + ".jpg"
        sucessSave = cv2.imwrite(folder + file_name, img)


        #if the picture recording failed
        if not sucessSave:
            logger.error("The picture could not be saved here : "+ folder+file_name )
            raise Exception(5)
        else:
            logger.info( "Picture has been saved in file : " + folder+file_name )
            PictureProcessing.writeTxtFile(logger, floucaptFolder, date, file_name)

#       exception 4  : The folder doesn't exist and could not be created
#       exception 5  : The picture could not be saved here




    @staticmethod
    def writeTxtFile(logger, floucaptFolder, date, fileName) :
        global oldPic
        try:
            oldPic
        except NameError:
            oldPic = ""

        try:
#            file = open("/var/www/FlouCapt2/conf/picture.txt", "w")
            file = open(floucaptFolder + "/conf/picture.txt", "w+")

            file.write("pictures/"+ date + "/" + fileName + "|")
            file.write(oldPic)
            file.close()
        except (RuntimeError, TypeError, NameError, IOError), e:
            logger.error("Unable to write picture.txt" + str(e) )

        oldPic = "pictures/"+ date + "/" + fileName

    @staticmethod
    def writeTxtFileError(logger, floucaptFolder, error) :

        try:
#            file = open("/var/www/fTest/conf/picture.txt", "w")
            file = open(floucaptFolder + "/conf/picture.txt", "w+")
            file.write( str(error) )
            file.close()
        except (RuntimeError, TypeError, NameError, IOError), e:
            logger.error("Unable to write picture.txt" + str(e))



