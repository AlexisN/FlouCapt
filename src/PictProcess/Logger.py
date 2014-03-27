#!/bin/env python2
# -*-coding:UTF-8 -*



import sys, time

class Logger:
    """

    """

    def info(self, message):
        date = self.hourAndMinute()
        sys.stdout.write("INFO  %s :  %s\n" %(date, message) )
        sys.stdout.flush()



    def debug(self, message):
        date = self.hourAndMinute()
        sys.stdout.write("DEBUG %s :  %s\n" %(date, message) )
        sys.stdout.flush()



    def error(self, message):
        date = self.hourAndMinute()
        sys.stderr.write("ERROR %s :  %s\n" %(date, message) )
        sys.stderr.flush()



    def hourAndMinute(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
