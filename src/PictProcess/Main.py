#!/usr/bin/python2

from PictureProcessing import *
from Camera import *
import sys, time, os, cv2

def savePicture( img ):
    date = time.strftime('%d-%m-%Y', time.localtime())
    hour = time.strftime('%H:%M:%S', time.localtime())

    folder = "out/"+ date + "/"

    #if the folder doesn't exist
    if not os.path.isdir( folder ):
        os.makedirs( folder )


    file_name = date + " " + hour + ".png"
    sucessSave = cv2.imwrite(folder + file_name, img)

    #if the picture recording failed
    if not sucessSave:
        print "The picture could not be saved here : "+ folder+file_name



if __name__ == '__main__':

    file_name = "img/lena.png"


    img = cv2.imread(file_name)
    if img == None:
        print("Image was not loaded.")
        sys.exit(-1)



    rects = PictureProcessing.detectFaces( img )
    img   = PictureProcessing.smoothFaces( rects, img )

    savePicture( img )
