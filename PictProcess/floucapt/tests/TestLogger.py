#!/bin/env python2
# -*-coding:UTF-8 -*


import unittest, sys, os
from datetime import date, timedelta, datetime
sys.path.append('..')
from Logger import Logger

class TestLogger(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()
        self.message = "Message"
        self.nameFi = 'logger.log'

    def tearDown(self):
        try:
            os.remove(self.nameFi)
        except Exception:
            pass



    def test_info(self):
        oldStdOut = sys.stdout
        #Redirection vers le fichier
        sys.stdout.flush()
        sys.stdout = open(self.nameFi, 'w+')


        self.logger.info( self.message )


        f = file(self.nameFi, 'r')
        mes = f.read()
        f.close()

        sys.stdout = oldStdOut
        self.assertNotEqual( mes.find(self.message), -1)
        self.assertNotEqual( mes.find("INFO"), -1)



    def test_error(self):
        oldStdErr = sys.stderr
        #Redirection vers le fichier
        sys.stderr.flush()
        sys.stderr = open(self.nameFi, 'w+')


        self.logger.error( self.message )

        sys.stderr = oldStdErr

        f = file(self.nameFi, 'r')
        mes = f.read()
        f.close()


        self.assertNotEqual( mes.find(self.message), -1)
        self.assertNotEqual( mes.find("ERROR"), -1)

    def test_date(self):

        string = self.logger.hourAndMinute()

        dateObj = datetime.strptime(string, '%Y-%m-%d %H:%M:%S')

        # Si le temps différe de plus de 1 seconde
        self.assertLess(datetime.now() - dateObj,  timedelta(seconds=1))




def main():
    unittest.main()


if __name__ == '__main__':
    main()



