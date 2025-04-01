import functools

class TypeCheckError(TypeError):
    pass

def type_check(expected_type):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(arg):
            if not isinstance(arg, expected_type):
                raise TypeCheckError(f"Expected argument of type {expected_type.__name__}, but got {type(arg).__name__}")
            return func(arg)
        return wrapper
    return decorator

# Example usage:
@type_check(int)
def square(n):
    return n * n


if __name__ == '__main__':
    square("4")  # This will raise TypeCheckError
