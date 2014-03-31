#!/bin/env python2
# -*-coding:UTF-8 -*



import sys, time

class Logger:
    """
    This classe allows to write a message in stdout or stderr depending on the type of the message
    The type of message, the date and time are added before the message

    If the message is a info message, you must call the method info
    If the message is an error message, you must call the method error

    stdout and stderr are usually redirected to log files
    """

    def info(self, message):
        """ Write a message in stdout (standard output)
            'INFO', the date and time are added before the message
        """
        date = self.hourAndMinute()
        sys.stdout.write("INFO  %s :  %s\n" %(date, message) )
        sys.stdout.flush()


    def error(self, message):
        """  Write a message in stderr (error output)
            'ERROR', the date and time are added before the message
        """
        date = self.hourAndMinute()
        sys.stderr.write("ERROR %s :  %s\n" %(date, message) )
        sys.stderr.flush()



    def hourAndMinute(self):
        """ Return date and hour in string
        """
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
