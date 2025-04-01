"""
This module provides the `cup_of_join` function, which joins multiple lists with a separator.
"""

def cup_of_join(*lists, sep=''):
    """
    Joins multiple lists with a separator between the lists.
    """
    if not lists:
        return None
    result = []
    for i, lst in enumerate(lists):
        result.extend(lst)  # Extend the result list with elements from the current list
        if sep != '':
            result.append(sep)  # Add separator after appending last list
    return result


if __name__ == '__main__':
    # Example usage
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
