#!/usr/bin/env python
'''
Simple logging for use in libraries
'''

__all__ = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'MyLibrary']

# Log levels
[DEBUG, INFO, WARNING, ERROR] = range(4)

class MyLibrary(object):
    def __init__(self, foo, logger_call_back):
        '''
        Library initialization function. Expects
        foo: an positive integer
        logger_call_back: Call back function for logging, logger_call_back(severity, string)
        '''
        if logger_call_back is None:
            raise self.MyLibraryException("logger call back cannot be None")
        self.logger_call_back = logger_call_back
        self.logger(DEBUG, "Setting logger to %r" %logger_call_back)
        self.foo = foo

    class MyLibraryException(Exception):
        '''
        Base class for all exceptions from this library
        '''
        pass
    
    def logger(self, severity, string):
        '''
        Internal library logger
        '''
        self.logger_call_back(severity, "%s::%s" %(self.__class__.__name__, 
            string))

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

if __name__ == "__main__":
    '''
    In code that imports the library
    '''
    # import MyLib
    # log_level = MyLib.DEBUG

    log_level = DEBUG

    def my_lib_logger(severity, string):
        '''
        My implementation specific logger
        '''
        # Map this to your own code's logger
        # In django, we'd do something like
        '''
        if severity == DEBUG:
            logger.debug(string)
        elif severity == INFO:
            logger.info(string)
        elif severity == WARNING:
            logger.warning(string)
        elif severity == ERROR:
            logger.error(string)
        '''
        if severity >= log_level:
            print string

    # Create an instance of the lib
    foo = 23
    lib_inst = MyLibrary(foo, my_lib_logger)

    # Call some library routine
    bar = 46
    lib_inst.do_some_lib_work(bar)
