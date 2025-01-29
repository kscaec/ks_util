# Various utility functions.

At this stage the following functions are implemented:
- ic_variants_with_log_levels

## ic_variants_with_log_levels

ic_variants_with_log_levels are based on icecream's ic(): https://github.com/gruns/icecream

The function variants add logging level capabilities to ic():
- They prefix the ic() output with a time stamp and a logging level.
- They write to both the console and a log file.
- (Format and log file can be modified as desired.)

The function variants are:
- icd logs a DEBUG message.
- ici logs an INFO message.
- icw logs a WARNING message.
- ice logs an ERROR message.
- icc logs a CRITICAL message.

Use the functions as you would use ic(). They internally use ic(), "as is".
- They are not wrapper functions if ic(), as this would lose the caller's context and hence the caller's variable names.
- Rather they add a _log method to icecream's IceCreamDebugger class to obtain logging level capabilities.

The functions (use and) conform to the Python logging module's logging levels: https://docs.python.org/3/library/logging.html#logging-levels\n

The minimum logging level is set in the line "file_handler.setLevel(logging.DEBUG)".
Replace DEBUG by whichever minimum level is preferred.

### Examples

#### INPUT
x = 10  
y = 20  
str = 'this is a very long string xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  
icd(x, y)  # This will log a DEBUG message with the caller's variable names  
ici()  
icw(10, 'hello', x)  
ice(x, x**2, x/2, str)  
icc('oops', x + y)  

#### OUTPUT
2025-01-29 17:04:30.859 DEBUG ic| x: 10, y: 20  
2025-01-29 17:04:30.860 INFO ic| ic_variants_for_log_levels.py:54 in <module> at 17:04:30.860  
2025-01-29 17:04:30.860 WARNING ic| 10, 'hello', x: 10  
2025-01-29 17:04:30.860 ERROR ic| x: 10  
2025-01-29 17:04:30.860 ERROR     x**2: 100  
2025-01-29 17:04:30.861 ERROR     x/2: 5.0  
2025-01-29 17:04:30.861 ERROR     str: ('this is a very long string '  
2025-01-29 17:04:30.861 ERROR           'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')  
2025-01-29 17:04:30.861 CRITICAL ic| 'oops', x + y: 30  