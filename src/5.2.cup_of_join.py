def cup_of_join(*lists, sep='-'):
    """
    Joins multiple lists with a separator between the lists.
    """
    if not lists:
        return None
    result = []
    for i, lst in enumerate(lists):
        if i > 0:
            result.append(sep)  # Add separator before appending next list
        result.extend(lst)  # Extend the result list with elements from the current list
    return result


if __name__ == '__main__':
    # Example usage
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep='@'))