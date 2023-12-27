import time 
# import the time and create a timer function that will accept function
def timer(func):
    # nested function that will accept function arguments
    def wrapper(*args, **kwargs):
        # then we create a variable that will get the time
        start_t = time.time()
        # then we create a variable that will get the result of the function
        result = (func(*args, **kwargs))
        # then we create another variable that will get the total time
        total_t = time.time() - start_t
        # then we print the total time
        print('{} took {} seconds'.format(func.__name__, total_t))
        # then we return the result
    return wrapper

# then we create a function that will accept two arguments
@timer
def sleep(a, b):
    print("Sleeping...")
    time.sleep(5)
    return a + b
# then we create a function that
print(sleep(1, 5))

#output
'''
Sleeping...
sleep took 5.001675128936768 seconds
None
'''