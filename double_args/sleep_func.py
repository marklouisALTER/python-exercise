import time
# we import the time and then create function that will accept two arguments
def sleep(a, b):
    print("Sleeping...") # print the sleeping string
    time.sleep(5) # sleep 5 seconds
    return a + b # return the sum of two arguments

print(sleep(1, 5))# print the function with with two arguments