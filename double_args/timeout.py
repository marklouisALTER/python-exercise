import signal
from functools import wraps
import time 

# I created a function that will accept variable n
def timeout(n):
    # I created a decorator function that will accept function
    def decorator(func):
        # I created a wrapper function that will accept arguments and keyword arguments
        @wraps(func)
        def wrapper(*args, **kwargs):
            # We use signal.alarm() to raise a signal after a specified number of seconds
            signal.alarm(n)
            # We use try and finally to execute the code
            try:
                return func(*args, **kwargs)
            finally:
                signal.alarm(0)
        # then we return the wrapper
        return wrapper
    # then we return the decorator
    return decorator

# then we create a function that will accept two arguments
@timeout(5)
def foo():
    time.sleep(10)
    print("foo!")

foo()


    