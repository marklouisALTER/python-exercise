
# We create function what will accept one aguments and we call it n variable
def print_n_times(n):
    # we create a decorator function that will accept function
    def decorator(func):
        # we create a wrapper function that will accept arguments and keyword arguments
        def wrapper(*args, **kwargs):
            # then we create a for loop that will loop through the range of n
            for _ in range(n):
                # then we return the function with arguments and keyword arguments
                func(*args, **kwargs)
        # then we return the wrapper
        return wrapper
    # then we return the decorator
    return decorator

# then we create a function that will accept two arguments
@print_n_times(5)

def sum(a, b):
    print(a + b)

print(sum(1, 5))

# @html("<div>", "</div>")
def goodbye(name):
    print("Goodbye {}".format(name))

print(goodbye("John"))