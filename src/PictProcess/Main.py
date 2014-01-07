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


    file_name = date + "-" + hour + ".jpg"
    sucessSave = cv2.imwrite(folder + file_name, img)

    #if the picture recording failed
    if not sucessSave:
        print "The picture could not be saved here : "+ folder+file_name
    else:
        print "Picture has been saved at "+date + "-"+ hour

def loadConfig():
    try:
        file = open("config.cfg", "r")
    except IOError:
        print 'The config file "config.cfg" cannot be open'

    else:

        for line in file:
            line = line.rstrip('\n\r')
            tab = line.split("=")

            if len(tab) != 2:
                continue
            #convert string to unicole for use isdecimal() method
            tab[1] = unicode(tab[1], 'utf-8')

            if tab[0]=="frequencyPictures" and tab[1].isdecimal():
                print "load frequencyPictures"
                freqPictures = int(tab[1])


        file.close()

    #frequencyPictures is a 20 seconds by default
    if freqPictures == None:
        freqPictures = 10

    return freqPictures


if __name__ == '__main__':


    loadConfig()

    while True:

        ok, img = Camera.getPicture()

        #if capture picture successful
        if ok:
            rects = PictureProcessing.detectFaces( img )
            img   = PictureProcessing.smoothFaces( rects, img )
            savePicture( img )

        # 30 seconds pause
        time.sleep(30)
