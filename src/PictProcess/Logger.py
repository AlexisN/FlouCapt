#!/bin/env python2
# -*-coding:UTF-8 -*



import sys

class Logger:
    """

    """



    def info(self, message):
        sys.stdout.write("INFO :    %s\n" % message)
        sys.stdout.flush()



    def debug(self, message):
        sys.stdout.write("DEBUG :    %s\n" % message)
        sys.stdout.flush()



    def error(self, message):
        sys.stderr.write("ERROR :    %s\n" % message)
        sys.stderr.flush()


