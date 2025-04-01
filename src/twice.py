"""
This module defines a decorator 'twice' that calls the decorated function twice.
"""

from decorator import decorator


@decorator
def twice(func, *args, **kwargs):
    """
    A decorator that calls the given function twice.

    :param func: The function to be decorated.
    :return: The wrapper function.
    """
    func(*args, **kwargs)
    return func(*args, **kwargs)


# Example usage:
@twice
def say_hello():
    """
    A simple function that prints 'Hello!'.
    """
    print("Hello!")


if __name__ == '__main__':
    say_hello()  # This will print "Hello!" twice
