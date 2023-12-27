
# We define the function two arguments it will multiply
def multiply(a, b):
    return a * b

# then we create another function that will accept a function
def double_args(func):
# we create another function inside the function its called nested function that accept two arguments
    def wrapper(a, b):
        # then multiply the two arguments to 2 then return it
        return func(a * 2, b * 2)
    # then it will return the output of the wrapper
    return wrapper
# we assign the double args and call the multiply function to multiply var
multiply = double_args(multiply)
#then we print the multiply function with two arguments
print(multiply(1, 5))