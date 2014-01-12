#!/usr/bin/python2

from PictureProcessing import *
from Camera import *
import sys, time, os, cv2, ConfigParser


def savePicture( img ):
    """
    Save the picture passed in parameter
    """

    date = time.strftime('%d-%m-%Y', time.localtime())
    hour = time.strftime('%H:%M:%S', time.localtime())

    folder = "out/"+ date + "/"

    #if the folder doesn't exist
    if not os.path.isdir( folder ):
        os.makedirs( folder )


    file_name = date + "-" + hour + ".jpg"
    sucessSave = cv2.imwrite(folder + file_name, img)

    #if the picture recording failed
    if not sucessSave:
        print "The picture could not be saved here : "+ folder+file_name
    else:
        print "Picture has been saved at "+date + "-"+ hour

def loadConfig():
    """
    Load a parameters since a config file (config.cfg)
    """
    config = ConfigParser.ConfigParser()
    config.read('config.cfg')

    try:
        freqPictures = config.getint('DEFAULT','frequencyPictures')
        print 'The config file has be loaded with success...'
    except ConfigParser.NoOptionError, ConfigParser.MissingSectionHeaderError:
        freqPictures = 10
        print 'The config file "config.cfg" cannot be opened\nor the data of "config.cfg" cannot be loaded'

    return freqPictures


if __name__ == '__main__':
    """
    The main function.
    Start a picture processing application.
    """

    freqPictures = loadConfig()

    while True:

        ok, img = Camera.getPicture()

        #if capture picture successful
        if ok:
            rects = PictureProcessing.detectFaces( img )
            img   = PictureProcessing.smoothFaces( rects, img )
            savePicture( img )

        # pause
        time.sleep(freqPictures)
