import time 
# import time and create time function that will accept a function
def memorize(func):
    # create a dictionary
    cache = {}
    # create a nested function that will accept two arguments
    def wrapper(*args, **kwargs):
        # if the arguments and keyword arguments is not in the cache
        if(args, kwargs) not in cache:
            # then we create a variable that will get the time
            cache[(args, kwargs)] = func(*args, **kwargs)
        # then we return the cache
        return cache[(args, kwargs)]
    # then we return the wrapper
    return wrapper

# then we create a function that will accept two arguments
@memorize
def sleep(a, b):
    print("Sleeping...")
    time.sleep(5)
    return a + b

# then we create a function that will accept two arguments
print(sleep(1, 5))

