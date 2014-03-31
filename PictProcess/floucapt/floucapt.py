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
    Load a parameters since a config file (/etc/floucapt/config.ini)
    The file must be contains a section [DEFAULT]
    and the follows parameters :
       frequencyPictures   : refresh time to recontact the camera in seconds (10 by default)
       link                : link to the video stream of camera (0 by default because it's a webcam)
       floucaptFolder      : The folder that contains the web application of Floucapt


    :param logger: Logger allow to write errors
    :return:    frequencyPictures, link, floucaptFolder

    """


    #Default values
    defFreqPictures = 10
    defLink = '0'
    defFloucaptFolder = 'out'

    try:
        parser = ConfigParser.ConfigParser()
        parser.read('config.ini')
    except ConfigParser.ParsingError, err:
        logger.error("Could not parse:" +  str(err) )
        return defFreqPictures, defLink, defFloucaptFolder


    try:
        freqPictures = parser.getint('DEFAULT','frequencyPictures')
    except ConfigParser.NoOptionError, ConfigParser.MissingSectionHeaderError:
        freqPictures = defFreqPictures
        logger.error("The parameter 'freqPictures' cannot be loaded from config.ini")


    try:
        link = parser.get('DEFAULT','link')
    except ConfigParser.NoOptionError, ConfigParser.MissingSectionHeaderError:
        link = defLink
        logger.error("The parameter 'link' cannot be loaded from config.ini")


    try:
        floucaptFolder = parser.get('DEFAULT','floucaptFolder')
    except ConfigParser.NoOptionError, ConfigParser.MissingSectionHeaderError:
        floucaptFolder = defFloucaptFolder
        logger.error("The parameter 'floucaptFolder' cannot be loaded from config.ini")



    return freqPictures, link, floucaptFolder





#Implementation of daemon
class DaemonImpl(Daemon):
    """
    This class is a concrete implementation of abstract
    daemon.
    """
    def __init__(self):
        Daemon.__init__(self, pidfile='/tmp/floucapt.pid', stdout='/tmp/floucapt.log', stderr='/tmp/floucapt.error')
        self.quit    = False
        self.logger  = Logger()
        self.cleaner = Cleaner()


    """

    """
    def signal_handler(self, signal, frame):
        self.quit = True

    """
    This method save the times for the next pause of application
    This variable will be used in the method time_diff()
    """
    def time_start(self):
        self.startTime = time.time()

    """
    This method calculate the remaining time before the next contact camera
    Then we put the application pauses

    With this, the real frequency of contact with the camera is exactly the same as defined in the config file
    """
    def time_diff(self):
        endTime = time.time()
        elapsed = endTime - self.startTime
        pause = self.freqPictures - elapsed

        if pause > 0:
            time.sleep(pause)


    """


    """
    def run(self):
        # Redirection of signal to close properly application
        signal.signal(signal.SIGINT , self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

        # Load the configuration from the config file
        self.freqPictures, link, floucaptFolder = loadConfig(self.logger)


        # Main loop
        # Handles contact with the camera,
        # processing and recording the image
        # the call to cleaner
        # the process to sleep
        #
        # and errors
        while not self.quit:

            # Save the time
            self.time_start()


            # Retrieve the image from Camera
            # Detection of humans faces
            # Blur faces
            # Save picture in folder
            try:
                img = Camera.getPicture( self.logger, link )

                rects = PictureProcessing.detectFaces( self.logger, img )
                img = PictureProcessing.smoothFaces( rects, img )
                PictureProcessing.savePicture( self.logger, floucaptFolder, img )

            except Exception, e:
                # if an error occurs, we write the error code in the file picture.txt
                PictureProcessing.writeTxtFileError(self.logger, floucaptFolder, e.args[0] )
                del e   # Delete varaible memory



            # Delete variables in memory
            try:
                del img
                del rects
            except NameError:
                pass


            # Call the cleaner
            # If the date has not changed, it does nothing
            self.cleaner.run(floucaptFolder)


            # If the quit signal was not sent
            # Then the application wait before the next contact of camera
            if not self.quit:
                self.time_diff()


"""
    The main function of application
    Take actions based on the first parameter : argv[1]

    First argument :
    'start'     -> Start the daemon if it's not already started
    'stop'      -> Stop the daemon, if daemon not running, return error
    'restart'   -> Restart the daemon
    'status'    -> Print the status of daemon ( Is running or not)
    'no-daemon' -> Execute the application without the daemon
"""
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

