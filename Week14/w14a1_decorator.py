"""The decorator pattern allows behavior to be added to an individual object,
dynamically, without affecting the behavior of other objects from the same class.
The decorator log_decorator adds logging functionality to the add function, allowing
you to see when the function is called and what it returns."""

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

# Personal example for confirmation of understanding
@log_decorator
def subt(a, b):
    return a - b

add(3, 5)
subt(10, 4)