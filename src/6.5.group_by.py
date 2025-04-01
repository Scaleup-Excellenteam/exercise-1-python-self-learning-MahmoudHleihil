from collections import defaultdict

def group_by(func, iterable):
    """
    Returns a dictionary where the keys are the values obtained by applying the function to the items,
    and the values are lists of items that correspond to each key.
    """
    grouped = defaultdict(list)  # defaultdict initializes a list if key doesn't exist
    for item in iterable:
        grouped[func(item)].append(item)  # Apply function to item and group by result
    return dict(grouped)  # Convert defaultdict back to a regular dictionary for the result


if __name__ == '__main__':
    # Example usage
    print(group_by(len, ["hi", "bye", "yo", "try"]))  # {2: ["hi", "yo"], 3: ["bye", "try"]}
