"""
This module provides the `parsle_tongue` function, which extracts secret messages from a binary file.
"""

import re


def parsle_tongue():
    """
    Extracts secret messages from a binary file.

    :param filename: Path to the binary file.
    :return: A list of extracted secret messages.
    """
    filename = "resources/logo.jpg"
    pattern = re.compile(rb'[a-z]{5,}!')  # Regex pattern to find secret messages
    messages = []

    with open(filename, 'rb') as file:
        while chunk := file.read(1024):  # Read in chunks to avoid memory overload
            # For each match found in the chunk, decode and add to the messages list
            messages.extend(match.group().decode() for match in pattern.finditer(chunk))

    return messages


if __name__ == '__main__':
    # Example usage
    print(parsle_tongue())
