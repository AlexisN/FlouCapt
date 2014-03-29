#!/bin/env python2
# -*-coding:UTF-8 -*


import unittest, sys, os, time
import cv2

sys.path.append('..')
from PictureProcessing import PictureProcessing

class Logger:
    def info(self, message):
        pass
    def debug(self, message):
        pass
    def error(self, message):
        pass



class TestPictureProcessing(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()
        os.chdir('..')
        #print "deb"

    def tearDown(self):
        os.chdir('tests')
        #print "fin"


    def test_detectFaces(self):
        img = cv2.imread("img/lena.png")
        if img == None:
            self.fail("Image was not loaded.")
            return
        try:
            rects = PictureProcessing.detectFaces( self.logger,  img )
        except:
            self.fail("The cascade classifier can't be loaded")
            return
        self.assertNotEqual( len(rects), 0 )



    def test_detectFaces2(self):
        os.chdir('tests')
        img = cv2.imread("../img/lena.png")
        if img == None:
            self.fail("Image was not loaded.")
            return
        try:
            rects = PictureProcessing.detectFaces( self.logger,  img )
            self.fail("The cascade classifier can be loaded and it's not normally")
        except Exception, e:
            self.assertEqual(e.args[0], 3)
        os.chdir('..')

    def test_savePicture(self):

        img = cv2.imread("img/lena.png")
        if img == None:
            self.fail("Image was not loaded.")
            return

        date = time.strftime('%Y-%m-%d', time.localtime())
        nb1 = os.popen('ls out/' + date + ' |wc -l')
        nb1= int( nb1.read() )

        try:
            PictureProcessing.savePicture(self.logger, img)
        except Exception, e:
            self.fail("savePicture raise exception of value : " + str(e.args[0]) )
            return

        #verif qu'il y a un fichier de plus
        nb2 = os.popen('ls out/' + date + ' |wc -l')
        nb2= int( nb2.read() )
        self.assertEqual(nb1+1, nb2)




    #Test : Le dossier d'enregistrement des images n'est pas accessible
    def test_savePicture2(self):

        img = cv2.imread("img/lena.png")
        if img == None:
            self.fail("Image was not loaded.")
            return

        os.chmod('out/', 0)

        try:

            PictureProcessing.savePicture(self.logger, img)
            #self.fail("savePicture not raise exception" )
            print "not exception"
        except Exception, e:
            self.assertEqual(e.args[0], 4)


        os.chmod('out/', 0755)


    #Test : Il est impossible d'écrire dans le dossier d'enregistrement des images
    def test_savePicture3(self):

        img = cv2.imread("img/lena.png")
        if img == None:
            self.fail("Image was not loaded.")
            return

        date = time.strftime('%Y-%m-%d', time.localtime())
        os.chmod('out/' + date + '/', 0555)
        time.sleep(0.7)



        try:

            PictureProcessing.savePicture(self.logger, img)
            #self.fail("savePicture not raise exception" )
            print "not exception"
        except Exception, e:
            self.assertEqual(e.args[0], 5)

        os.chmod('out/' + date + '/', 0755)





def main():
    unittest.main()


if __name__ == '__main__':
    main()



