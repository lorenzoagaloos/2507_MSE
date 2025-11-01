"""Using the decorator to implement time sleep funtion.
This demonstrates the sleep function from the time module.
It allows you to pause the execution of your program for a specified number of seconds."""

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} function with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Running {func.__name__} function returns: {result}\n")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

# Personal example for confirmation of understanding
@log_decorator
def subt(a, b):
    return a - b

# Another example
@log_decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Using time decorator
@log_decorator
def sleep_function(seconds):
    import time
    time.sleep(seconds)
    return f"Slept for {seconds} seconds"


add(3, 5)
sleep_function(2)

subt(10, 4)
sleep_function(3)

greet("Alice")
sleep_function(4)