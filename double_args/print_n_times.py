
def print_n_times(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@print_n_times(5)
def sum(a, b):
    print(a + b)

print(sum(1, 5))

# @html("<div>", "</div>")
def goodbye(name):
    print("Goodbye {}".format(name))

print(goodbye("John"))