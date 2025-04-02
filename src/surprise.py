"""
This module contains a decorator called 'surprise' that modifies functions
to print a surprise message before executing them.
"""

import functools


def surprise(func):
    """
    A decorator that prints 'surprise!' before calling the decorated function.

    :param func: The function to be decorated.
    :return: The wrapper function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        The wrapper function that prints 'surprise!' and then calls the original function.

        :param args: Positional arguments to be passed to the original function.
        :param kwargs: Keyword arguments to be passed to the original function.
        """
        print("surprise!")
        return func(*args, **kwargs)  # Ensure the original function is called

    return wrapper


# Example usage:
@surprise
def greet():
    """
    Prints a greeting message.
    """
    print("Hello, world!")


if __name__ == '__main__':
    greet()  # This will print "surprise!" followed by "Hello, world!"
