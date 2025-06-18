import logging
import os
from icecream import IceCreamDebugger
from datetime import datetime
import inspect
import functools
import time


# Configure the logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Create a file handler and set the logging level.
# 'w' mode will overwrite the logfile at every run.
file_handler = logging.FileHandler('../log_file.log', mode='w')
file_handler.setLevel(logging.DEBUG)

# Create a custom formatter for the file handler
file_formatter = logging.Formatter('%(asctime)s.%(msecs)03d %(levelname)s %(message)s',
                                   datefmt='%Y-%m-%d %H:%M:%S'
                                   )
file_handler.setFormatter(file_formatter)
# Add the handlers to the logger
logging.getLogger().addHandler(file_handler)

# Create a subclass of IceCreamDebugger to support logging
class IceCreamDebuggerWithLogging(IceCreamDebugger):
    def __init__(self, level, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.outputFunction = self._log
        self.level = level

    def _log(self, message):
        # Get the calling frame information
        frame = inspect.currentframe()
        try:
            # Go up two frames: one for _log, one for the IceCreamDebugger's method
            caller_frame = frame.f_back.f_back
            caller_info = inspect.getframeinfo(caller_frame)
            
            # Format the message to include file and line number
            filename = os.path.basename(caller_info.filename)
            line_no = caller_info.lineno
            function = caller_info.function
            
            # Get current time once for consistent timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            
            # Format the header line with timestamp
            header = f"{timestamp} {logging.getLevelName(self.level)} {filename}:{line_no} in {function}()"
            
            # Log the header
            print(header)
            
            # Log the message indented with spaces instead of timestamp
            for line in message.split('\n'):
                print(' ' * (len(timestamp) + 1) + line)
                
            # Also log to file handler if needed
            for handler in logging.getLogger().handlers:
                if isinstance(handler, logging.FileHandler):
                    handler.stream.write(header + '\n')
                    for line in message.split('\n'):
                        handler.stream.write(' ' * (len(timestamp) + 1) + line + '\n')
                    handler.stream.flush()
                    
        finally:
            # Important: delete the frame reference to avoid reference cycles
            del frame

ic = IceCreamDebugger()

icd = IceCreamDebuggerWithLogging(logging.DEBUG)  # DEBUG
ici = IceCreamDebuggerWithLogging(logging.INFO)  # INFO
icw = IceCreamDebuggerWithLogging(logging.WARNING)  # WARNING
ice = IceCreamDebuggerWithLogging(logging.ERROR)  # ERROR
icc = IceCreamDebuggerWithLogging(logging.CRITICAL)  # FATAL

# Example usage to test logging
if __name__ == '__main__':
    # Run some test examples.
    for i in range(10):
        x = 10
        y = 20
        str = 'this is a very long string xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        icd(x, y)  # This will log a DEBUG message with the caller's variable names
        ici()
        icw(10, 'hello', x)
        ice(x, x**2, x/2, str)
        icc('oops', x + y)  # This will log CRITCAL error with the caller's variable names
        # Delay
        time.sleep(0.1)
