#!/usr/bin/python2

from PictureProcessing import *
import sys
from cv2.cv import *


if __name__ == '__main__':

    file_name = "img/lena.png"


    img = cv2.imread(file_name)
    if img == None:
        print("Image was not loaded.")
        sys.exit(-1)


    rects = PictureProcessing.detect( img )
    PictureProcessing.box(rects, img)
