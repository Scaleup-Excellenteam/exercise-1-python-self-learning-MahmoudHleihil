"""
This module defines a decorator 'type_check' that checks if an argument matches the expected type.
"""

import functools


class TypeCheckError(TypeError):
    """
    Custom exception raised when an argument type does not match the expected type.
    """
    # No need for 'pass' here


def type_check(expected_type):
    """
    A decorator that checks if an argument matches the expected type.

    :param expected_type: The expected type for the argument.
    :return: The decorator function.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(arg):
            """
            The wrapper function that checks the argument type before calling the original function.

            :param arg: The argument passed to the decorated function.
            :raises TypeCheckError: If the argument type does not match the expected type.
            :return: The result of the decorated function.
            """
            if not isinstance(arg, expected_type):
                raise TypeCheckError(
                    f"Expected argument of type {expected_type.__name__}, "
                    f"but got {type(arg).__name__}"
                )
            return func(arg)

        return wrapper

    return decorator


# Example usage:
@type_check(int)
def square(n):
    """
    Returns the square of a given integer.

    :param n: An integer number.
    :return: The square of the given number.
    """
    return n * n


if __name__ == '__main__':
    square("4")  # This will raise TypeCheckError
