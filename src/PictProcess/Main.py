#!/usr/bin/python2

from PictureProcessing import *
from Camera import *
import sys, time, os, cv2, ConfigParser
#



"""
Load a parameters since a config file (config.cfg)
"""

config = ConfigParser.ConfigParser()
config.read('config.cfg')
    
try:
    frequency = config.getint('DEFAULT','frequencyPictures')
    link = config.get('DEFAULT','link')
    print 'The config file has be loaded with success...'
except ConfigParser.NoOptionError, ConfigParser.MissingSectionHeaderError:
    freqPictures = 10
    link = 0
    print 'The config file "config.cfg" cannot be opened\nor the data of "config.cfg" cannot be loaded'





if __name__ == '__main__':
    """
The main function.
Start a picture processing application.
"""

    freqPictures = frequency

    while True:

        ok, img = Camera.getPicture( link )
        print link

        #if capture picture successful
        if ok:
            rects = PictureProcessing.detectFaces( img )
            img = PictureProcessing.smoothFaces( rects, img )
            PictureProcessingsavePicture( img )

        # pause
        time.sleep(freqPictures)

    if hour = "00:00:00":
        cleaner.delete()
        cleaner.zipper()
    else:
        print "Error delete the folder containing the picture of 4 days"


