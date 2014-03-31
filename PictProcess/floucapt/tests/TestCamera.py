#!/bin/env python2
# -*-coding:UTF-8 -*


import unittest, sys, os, time
import cv2

sys.path.append('..')
from Camera import Camera

class Logger:
    def info(self, message):
        pass
    def error(self, message):
        pass



class TestCamera(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()

    def tearDown(self):
        pass





    def test_getPicture(self):

        try:
            Camera.getPicture(self.logger, 10000)
            print "Not exception"
        except Exception, e:
            self.assertEqual(e.args[0], 2)






def main():
    unittest.main()


if __name__ == '__main__':
    main()



