from ks_util import icd, ici, icw, ice, icc

def test_function():
    icd()

    x = 10
    y = 20
    
    # Test different log levels
    icd("Debug message", x, y)  # Debug level
    ici("Info message")         # Info level
    icw("Warning message")      # Warning level
    
    try:
        1/0
    except Exception as e:
        ice("Error occurred:", e)  # Error level
    
    icc("Critical message")  # Critical level

if __name__ == "__main__":
    print("Testing logging functions...")
    test_function()
    print("Check 'log_file.log' for the output")
