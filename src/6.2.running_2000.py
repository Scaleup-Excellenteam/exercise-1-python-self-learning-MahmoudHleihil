import time

def timer(f, *args, **kwargs):
    """
    Measures the execution time of the given function with the provided parameters.
    """
    start_time = time.perf_counter()  # Start the timer
    result = f(*args, **kwargs)       # Call the function with the provided arguments
    end_time = time.perf_counter()    # Stop the timer
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    return elapsed_time, result      # Return the time and the result of the function


if __name__ == '__main__':
    # Example usage
    print(timer(sum, [1, 2, 3, 4, 5]))