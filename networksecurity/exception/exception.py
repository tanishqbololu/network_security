import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self, error_message):
        self.error_message = error_message
        _,_,exc_tb = sys.exc_info() ## exc_tb is a traceback object, which contains:file name, line number, function name, call stack
        
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

        def __str__(self):
            return f"Error occured in python script name {self.file_name} line number {self.lineno} error message {str(self.error_message)} "
        