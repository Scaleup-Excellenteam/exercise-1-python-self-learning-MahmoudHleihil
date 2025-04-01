"""
This module provides a function to measure the execution time of a given function.
"""

import time


def running_2000(f, *args, **kwargs):
    """
    Measures the execution time of the given function with the provided parameters.

    :param f: The function to be executed.
    :param args: Positional arguments to pass to the function.
    :param kwargs: Keyword arguments to pass to the function.
    :return: A tuple containing the elapsed time and the function's return value.
    """
    start_time = time.perf_counter()  # Start the timer
    result = f(*args, **kwargs)  # Call the function with the provided arguments
    end_time = time.perf_counter()  # Stop the timer
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    return elapsed_time  # Return the time and the result of the function


if __name__ == '__main__':
    # Example usage
    print(running_2000(sum, [1, 2, 3, 4, 5]))
