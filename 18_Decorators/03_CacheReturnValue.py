# Implement a decorator that caches the return value of a function, so that when it 
# is called with the same arguments, the cached value is returned instead of re-
# executing the function
import time
from functools import wraps  # Optional, but recommended

def cache(func):
    cached_value = {}  # Dictionary to store cached results
    def wrapper(*args):
        if args in cached_value:
            print(f"Using cached value for {args}")
            return cached_value[args]
        print(f"Calculating result for {args}")
        result = func(*args)
        cached_value[args] = result
        return result

    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)  # Simulate long computation
    return a + b

# Test cases
print(long_running_function(4, 3))  # Takes 4 seconds
print(long_running_function(2, 6))  # Takes 4 seconds
print(long_running_function(4, 3))  # Instant, from cache
