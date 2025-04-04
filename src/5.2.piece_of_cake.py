"""
This module provides the `piece_of_cake` function, which calculates the total cost of ingredients needed for a recipe.
"""


def piece_of_cake(prices, optionals=None, **ingredients):
    """
    Calculates the total price of the ingredients needed for a recipe.

    :param prices: Dictionary where keys are ingredient names and values are price per 100 grams.
    :param optionals: List of optional ingredients to be ignored.
    :param ingredients: Keyword arguments specifying the quantity (in grams) for each ingredient.
    :return: Total cost of the required ingredients.
    """
    if not prices:
        return 0

    if optionals is None:
        optionals = []

    total_price = sum(
        (amount / 100) * prices[item]
        for item, amount in ingredients.items() if item in prices and item not in optionals
    )

    return int(total_price)  # Ensuring integer output


if __name__ == '__main__':
    # Example usage
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))  # Output: 44
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))  # Output: 54
    print(piece_of_cake({}))  # Output: 0
