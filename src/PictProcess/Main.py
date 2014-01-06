#!/usr/bin/python2

from PictureProcessing import *
from Camera import *
import sys, time, cv2

def savePicture( img ):
    date = time.strftime('%d-%m-%y', time.localtime())
    hour = time.strftime('%H:%M:%S', time.localtime())

    folder = "out/"
    file_name = date + " " + hour + ".png"

    cv2.imwrite(folder + file_name, img)




if __name__ == '__main__':

    file_name = "img/lena.png"


    img = cv2.imread(file_name)
    if img == None:
        print("Image was not loaded.")
        sys.exit(-1)



    rects = PictureProcessing.detectFaces( img )
    img   = PictureProcessing.smoothFaces( rects, img )

    savePicture( img )
