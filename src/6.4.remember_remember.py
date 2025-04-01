"""
This module provides a function to decode a hidden message from an image where each column contains one black pixel.
"""
import os

from PIL import Image


def remember_remember(image_path):
    """
    Decodes a hidden message from an image where each column contains one black pixel.

    :param image_path: Path to the encrypted image file.
    :return: The decoded secret message.
    """
    with Image.open(image_path).convert("L") as img:  # Open file inside function
        width, height = img.size
        message = ""

        for x in range(width):
            for y in range(height):
                if img.getpixel((x, y)) == 1:  # Black pixel found
                    message += chr(y)  # Convert row index to character
                    break

    return message


if __name__ == '__main__':
    # Example usage
    img_path = os.path.join(os.path.dirname(__file__), '../src/code.png')
    print(remember_remember(img_path))
