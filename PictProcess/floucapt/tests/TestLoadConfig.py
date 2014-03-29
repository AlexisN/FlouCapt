#!/bin/env python2
# -*-coding:UTF-8 -*


import unittest, sys, os, shutil
import cv2

sys.path.append('..')
from floucapt import loadConfig

class Logger:
    def info(self, message):
        pass
    def debug(self, message):
        pass
    def error(self, message):
        pass



class TestCamera(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()
        os.chdir('..')
        #Sauvegarde du config.ini actuel
        shutil.copy('config.ini', 'tests/config.ini')

    def tearDown(self):
         #Restauration du config.ini original
        shutil.copy('tests/config.ini', 'config.ini')
        os.remove('tests/config.ini')
        os.chdir('tests')



    def test_loadConfig(self):

        f = open('config.ini','w+')
        f.write(
        """[DEFAULT]
        """)
        f.close()

        self.assertEqual(loadConfig(self.logger), (10, '0', 'out'))

    def test_loadConfig_2(self):

        os.remove('config.ini')

        self.assertEqual(loadConfig(self.logger), (10, '0', 'out'))


    def test_loadConfig_3(self):

        f = open('config.ini','w+')
        f.write( "" )
        f.close()

        self.assertEqual(loadConfig(self.logger), (10, '0', 'out'))


    def test_loadConfig_4(self):

        f = open('config.ini','w+')
        f.write( '[DEFAULT]\nlink = 5\n' )
        f.close()

        self.assertEqual(loadConfig(self.logger), (10, '5', 'out'))



    def test_loadConfig_5(self):

        f = open('config.ini','w+')
        f.write( "[DEFAULT]\nlink = http://www.google.fr\n" )
        f.close()

        self.assertEqual(loadConfig(self.logger), (10, 'http://www.google.fr', 'out'))


    def test_loadConfig_6(self):

        f = open('config.ini','w+')
        f.write( "[DEFAULT]\nfrequencyPictures = 15\n")
        f.close()

        self.assertEqual(loadConfig(self.logger), (15, '0', 'out'))

    def test_loadConfig_7(self):

        f = open('config.ini','w+')
        f.write( "[DEFAULT]\nfloucaptFolder = folder\n")
        f.close()

        self.assertEqual(loadConfig(self.logger), (10, '0', 'folder'))


    def test_loadConfig_all(self):

        f = open('config.ini','w+')
        f.write( "[DEFAULT]\n"
               + "frequencyPictures = 15\n"
               + "link = http://www.google.fr\n"
               + "floucaptFolder = folder\n")
        f.close()

        self.assertEqual(loadConfig(self.logger), (15, 'http://www.google.fr', 'folder'))



def main():
    unittest.main()


if __name__ == '__main__':
    main()



