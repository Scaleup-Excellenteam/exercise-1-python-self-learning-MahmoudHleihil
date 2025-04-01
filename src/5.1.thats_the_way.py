import os

"""
This module contains a function to list files in a directory that start with 'deep'.
"""

def thats_the_way(directory: str):
    """
    Returns a list of all files in the given directory that start with 'deep'.
    """
    return [
        file for file in os.listdir(directory)
        if file.startswith("deep") and os.path.isfile(os.path.join(directory, file))
    ]


if __name__ == '__main__':
    # Example usage
    print(thats_the_way("./images"))
