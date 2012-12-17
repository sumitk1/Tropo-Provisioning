#!/usr/bin/env python
'''
Simple logging for use in libraries
'''

__all__ = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'TropoLogger']

# Log levels
[DEBUG, INFO, WARNING, ERROR] = range(4)

class TropoLogger(object):
    def __init__(self, foo, logger_call_back):
        '''
        Library initialization function. Expects
        foo: an positive integer
        logger_call_back: Call back function for logging, logger_call_back(severity, string)
        '''
        if logger_call_back is None:
            raise self.TropoLoggerException("logger call back cannot be None")
        self.logger_call_back = logger_call_back
        self.logger(DEBUG, "Setting logger to %r" %logger_call_back)
        self.foo = foo

    class TropoLoggerException(Exception):
        '''
        Base class for all exceptions from this library
        '''
        pass
    
    def logger(self, severity, string):
        '''
        Internal library logger
        '''
        self.logger_call_back(severity, "%s::%s" %(self.__class__.__name__, string))

    def do_some_lib_work(self, bar):
        '''
        Library function
        Returns True if successful
        '''
        self.logger(DEBUG, "DEBUG: This is a debug message")
        self.logger(INFO, "INFO: FYI foo = %r bar = %r" %(self.foo, bar))
        self.logger(WARNING, "WARNING: Something is not right")
        self.logger(ERROR, "ERROR: An error irrecoverable error has happened")
        return True


