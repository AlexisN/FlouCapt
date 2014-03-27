#!/bin/env python2
# -*-coding:UTF-8 -*

from Cleaner import *
from PictureProcessing import *
from Camera import *
from Daemon import Daemon
from Logger import Logger
import time, sys, cv2, ConfigParser, signal


def loadConfig(logger) :
    """
    Load a parameters since a config file (config.ini)
    """

#    config = ConfigParser.ConfigParser()
#    config.read('config.ini')
#
#    try:
#        freqPictures = config.getint('DEFAULT','frequencyPictures')
#        link = config.get('DEFAULT','link')
#        logger.info( "The config file has be loaded with success..." )
#    except ConfigParser.NoOptionError, ConfigParser.MissingSectionHeaderError:
#        freqPictures = 10
#        link = 0
#        logger.error(   """The config file "config.ini" cannot be opened
#                           or the data of "config.ini" cannot be loaded""" )



    try:
        parser = ConfigParser.SafeConfigParser()
        parser.read('config.ini')
    except ConfigParser.ParsingError, err:
        print 'Could not parse:', err
        return 10, '0'

    try:
        freqPictures = parser.getint('DEFAULT','frequencyPictures')
    except ConfigParser.NoOptionError, ConfigParser.MissingSectionHeaderError:
        freqPictures = 10
    try:
        link = parser.get('DEFAULT','link')
    except ConfigParser.NoOptionError, ConfigParser.MissingSectionHeaderError:
        link = '0'


    return freqPictures, link





#Implementation of daemon
class DaemonImpl(Daemon):
    '''
    This class is a concrete implementation of abstract
    daemon.
    '''
    def __init__(self):
        Daemon.__init__(self, pidfile='/tmp/floucapt.pid', stdout='/tmp/floucapt.log', stderr='/tmp/floucapt.error')
        self.quit = False
        self.logger = Logger()

    def signal_handler(self, signal, frame):
        self.quit = True

    def time_start(self):
        self.startTime = time.time()

    def time_diff(self):
        endTime = time.time()
        elapsed = endTime - self.startTime
        pause = self.freqPictures - elapsed

        if pause > 0:
            time.sleep(pause)



    def run(self):
        signal.signal(signal.SIGINT , self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

        self.freqPictures, link = loadConfig(self.logger)

        while not self.quit:

            self.time_start()

            try:
                img = Camera.getPicture( self.logger, link )

                rects = PictureProcessing.detectFaces( self.logger, img )
                img = PictureProcessing.smoothFaces( rects, img )
                PictureProcessing.savePicture( self.logger, img )

            except Exception, e:
                PictureProcessing.writeTxtFileError( e.args[0] )
                del e   # For memory

            # Delete variables in memory
            try:
                del img
                del rects
            except NameError:
                pass


            if not self.quit:
                # pause
                self.time_diff()



def main(argv):

    daemon = DaemonImpl()

    if len(argv) == 2:
        if 'start' == argv[1]:

                daemon.start()
        elif 'stop' == argv[1]:
                daemon.stop()
        elif 'restart' == argv[1]:
                daemon.restart()
        elif 'status' == argv[1]:
                daemon.status()
        elif 'no-daemon' == argv[1]:
                daemon.run()
        else:
            print 'Unknown command'
            sys.exit(2)
        sys.exit(0)
    # Print some help
    else:
        print "usage: %s start|stop|status|restart|no-daemon" % argv[0]
        sys.exit(2)


if __name__ == '__main__':
    main(sys.argv)

