#!/bin/env python2

from Cleaner import *
from PictureProcessing import *
from Camera import *
from daemon import Daemon
from Logger import Logger
import time, sys, cv2, ConfigParser, signal


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



def signal_handler(signal, frame):
    global quit
    quit = True



def run(logger):
    """
    The main function.
    Start a picture processing application.
    """
    global quit
    quit = False
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)


    freqPictures, link = loadConfig()

    while not quit:

        ok, img = Camera.getPicture( link )

        #if capture picture successful
        if ok:
            rects = PictureProcessing.detectFaces( logger, img )
            img = PictureProcessing.smoothFaces( rects, img )
            PictureProcessing.savePicture( logger, img )

        if not quit:
            # pause
            time.sleep(freqPictures)

        #Cleaner.run()



#Implementation of daemon
class DaemonImpl(Daemon):
    '''
    This class is a concrete implementation of abstract
    daemon.
    '''
    def __init__(self, pidfile, logger):
        Daemon.__init__(self, pidfile, stdout='/tmp/floucapt.log', stderr='/tmp/floucapt.log')
        self.quit = False
        self.logger = logger

    def signal_handler(self, signal, frame):
        self.quit = True

    def run(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

        freqPictures, link = loadConfig()

        while not self.quit:

            ok, img = Camera.getPicture( link )

            #if capture picture successful
            if ok:
                rects = PictureProcessing.detectFaces( self.logger, img )
                img = PictureProcessing.smoothFaces( rects, img )
                PictureProcessing.savePicture( self.logger, img )

            if not self.quit:
                # pause
                time.sleep(freqPictures)





def main(argv):

    logger = Logger()
    daemon = DaemonImpl('/tmp/floucapt.pid', logger)

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
                run(logger)
        else:
            print 'Unknown command'
            sys.exit(2)
        sys.exit(0)
    # Print some help
    else:
        print "usage: %s start|stop|status|restart" % argv[0]
        sys.exit(2)


if __name__ == '__main__':
    main(sys.argv)

