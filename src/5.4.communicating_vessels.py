import itertools

def interleave(*iterables):
    """
    Returns a list of interwoven elements from the given iterables.
    """
    return [item for items in itertools.zip_longest(*iterables, fillvalue=None) for item in items if item is not None]

# Example usage
print(interleave('abc', [1, 2, 3], ('!', '@', '#')))


def interleave_generator(*iterables):
    """
    A generator that yields interwoven elements from the given iterables.
    """
    for items in itertools.zip_longest(*iterables, fillvalue=None):
        for item in items:
            if item is not None:
                yield item


if __name__ == '__main__':
    # Example usage
    print(list(interleave_generator('abc', [1, 2, 3], ('!', '@', '#'))))
