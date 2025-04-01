"""
This module provides a function to analyze word lengths in a given text.
"""


def long_cat_is_long(text: str):
    """
    Returns a dictionary with the lengths of words in the given text.

    :param text: A string containing words to analyze.
    :return: A dictionary mapping words to their respective lengths.
    """
    # Clean up the text by removing non-alphabetic characters and converting to lowercase
    words = [''.join(char for char in word if char.isalpha()) for word in text.lower().split()]
    # Create a dictionary where the key is the word and the value is its length
    return {word: len(word) for word in words if word}  # Ensure non-empty words are considered


if __name__ == '__main__':
    # Example usage
    print(long_cat_is_long("You see, wire telegraph is a kind of a very, very long cat."))
