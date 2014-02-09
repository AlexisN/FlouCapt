#!/bin/env python2

from Cleaner import *
from PictureProcessing import *
from Camera import *
import time, cv2, ConfigParser


def loadConfig() :
    """
    Load a parameters since a config file (config.cfg)
    """

    config = ConfigParser.ConfigParser()
    config.read('config.cfg')

    try:
        freqPictures = config.getint('DEFAULT','frequencyPictures')
        link = config.get('DEFAULT','link')
        print 'The config file has be loaded with success...'
    except ConfigParser.NoOptionError, ConfigParser.MissingSectionHeaderError:
        freqPictures = 10
        link = 0
        print 'The config file "config.cfg" cannot be opened\nor the data of "config.cfg" cannot be loaded'
    return freqPictures, link




if __name__ == '__main__':
    """
    The main function.
    Start a picture processing application.
    """

    freqPictures, link = loadConfig()
    while True:

        ok, img = Camera.getPicture( link )

        #if capture picture successful
        if ok:
            rects = PictureProcessing.detectFaces( img )
            img = PictureProcessing.smoothFaces( rects, img )
            PictureProcessing.savePicture( img )
            #fichier = open(Current, "w")
            #fichier.write( img )
        # pause
        time.sleep(freqPictures)

        #Cleaner.run()


