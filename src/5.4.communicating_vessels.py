"""
This module provides functions to interleave elements from multiple iterables.
"""

import itertools


def interleave(*iterables):
    """
    Returns a list of interwoven elements from the given iterables.

    :param iterables: Multiple iterable objects.
    :return: A list of interwoven elements.
    """
    return [item for items in itertools.zip_longest(*iterables, fillvalue=None) for item in items if item is not None]


# Example usage
print(interleave('abc', [1, 2, 3], ('!', '@', '#')))


def generator_interleave(*iterables):
    """
    A generator that yields interwoven elements from the given iterables.

    :param iterables: Multiple iterable objects.
    :yield: Elements interwoven from the provided iterables.
    """
    for items in itertools.zip_longest(*iterables, fillvalue=None):
        for item in items:
            if item is not None:
                yield item


if __name__ == '__main__':
    # Example usage
    print(list(generator_interleave('abc', [1, 2, 3], ('!', '@', '#'))))
