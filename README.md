# ks_util - Enhanced Logging Utilities

A collection of utility functions with a focus on enhanced logging capabilities.

## Features

### ic_variants_with_log_levels

Enhanced logging functions based on [icecream](https://github.com/gruns/icecream)'s `ic()` with additional features:

- **Logging Levels**: Each function maps to a standard logging level
- **Caller Information**: Automatically includes file, line number, and function name
- **Clean Output**: Formatted for readability with proper indentation
- **Dual Output**: Writes to both console and log file (`log_file.log` by default)

### Available Functions

- `icd()` - DEBUG level logging
- `ici()` - INFO level logging
- `icw()` - WARNING level logging
- `ice()` - ERROR level logging
- `icc()` - CRITICAL level logging
- `ic` - Standard icecream debug function (unchanged)

## Installation

```bash
pip install -e .
```

## Usage

```python
from ks_util import icd, ici, icw, ice, icc, ic

def example_function():
    x = 10
    y = 20
    
    icd("Debug message", x, y)  # Debug level
    ici("Info message")          # Info level
    icw("Warning message")       # Warning level
    
    try:
        1/0
    except Exception as e:
        ice("Error occurred:", e)  # Error level
    
    icc("Critical message")  # Critical level
```

### Example Output

```
2025-06-18 20:26:11.317 DEBUG test_logging.py:4 in test_function()
                        ic| test_logging.py:4 in test_function() at 20:26:11.316
2025-06-18 20:26:11.332 DEBUG test_logging.py:10 in test_function()
                        ic| 'Debug message', x: 10, y: 20
2025-06-18 20:26:11.332 INFO test_logging.py:11 in test_function()
                        ic| 'Info message'
2025-06-18 20:26:11.332 WARNING test_logging.py:12 in test_function()
                        ic| 'Warning message'
2025-06-18 20:26:11.333 ERROR test_logging.py:17 in test_function()
                        ic| 'Error occurred:', e: ZeroDivisionError('division by zero')
2025-06-18 20:26:11.333 CRITICAL test_logging.py:19 in test_function()
                        ic| 'Critical message'
```

## Configuration

- Log file location: `log_file.log` (in the current working directory)
- Minimum log level: Set in `ic_variants_with_log_levels.py` (default: DEBUG)
- Log format: Customizable in the `_log` method

## Dependencies

- Python 3.6+
- icecream >= 2.1.4