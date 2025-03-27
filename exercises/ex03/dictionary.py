"""Some functions for working with dictionaries."""

__author__ = "730565431" 

def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary. Raises KeyError if duplicate values exist."""
    result: dict[str, str] = {}
    for key in input_dict:
        value = input_dict[key]
        if value in result:
            raise KeyError(f"Duplicate key found after inversion: {value}")
        result[value] = key
    return result

def count(values: list[str]) -> dict[str, int]:
    """Return a dictionary with counts of each unique string in the input list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

def favorite_color(favorites: dict[str, str]) -> str:
    """Returns the color that appears most frequently in the dictionary of favorite colors."""
    color_counts: dict[str, int] = count(list(favorites.values()))
    max_count: int = 0
    fav_color: str = ""
    for color in favorites.values():
        if color_counts[color] > max_count:
            max_count = color_counts[color]
            fav_color = color
    return fav_color

def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins a list of strings into a dictionary by string length."""
    result: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length in result:
            result[length].add(word)
        else:
            result[length] = {word}
    return result
