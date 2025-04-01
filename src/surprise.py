import functools

def surprise(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("surprise!")
    return wrapper

# Example usage:
@surprise
def greet():
    print("Hello, world!")


if __name__ == '__main__':
    greet()  # This will print "surprise!" instead of "Hello, world!"
