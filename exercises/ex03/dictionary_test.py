"""Unit tests for dictionary functions."""

__author__ = "730565431" 

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len
import pytest


# -------- invert() tests --------

def test_invert_use_case_1() -> None:
    """Invert a simple dictionary with unique values."""
    assert invert({"a": "x", "b": "y"}) == {"x": "a", "y": "b"}

def test_invert_use_case_2() -> None:
    """Invert a dictionary with more entries."""
    assert invert({"one": "uno", "two": "dos", "three": "tres"}) == {"uno": "one", "dos": "two", "tres": "three"}

def test_invert_edge_case_empty_dict() -> None:
    """Invert an empty dictionary."""
    assert invert({}) == {}


# -------- count() tests --------

def test_count_use_case_1() -> None:
    """Count frequencies of strings in a short list."""
    assert count(["a", "b", "a"]) == {"a": 2, "b": 1}

def test_count_use_case_2() -> None:
    """Count with all unique values."""
    assert count(["x", "y", "z"]) == {"x": 1, "y": 1, "z": 1}

def test_count_edge_case_empty_list() -> None:
    """Count with an empty list."""
    assert count([]) == {}


# -------- favorite_color() tests --------

def test_favorite_color_use_case_1() -> None:
    """Most common color should be returned."""
    assert favorite_color({"a": "blue", "b": "red", "c": "blue"}) == "blue"

def test_favorite_color_use_case_2() -> None:
    """Tie case - first color in dict order should win."""
    assert favorite_color({"a": "green", "b": "blue", "c": "blue", "d": "green"}) == "green"

def test_favorite_color_edge_case_single_entry() -> None:
    """Only one entry in the dictionary."""
    assert favorite_color({"a": "red"}) == "red"


# -------- bin_len() tests --------

def test_bin_len_use_case_1() -> None:
    """Test with mixed strings and check correct lengths."""
    assert bin_len(["apple", "bat", "carrot"]) == {5: 1, 3: 1, 6: 1}

def test_bin_len_use_case_2() -> None:
    """Test with duplicates and varying lengths."""
    assert bin_len(["a", "bb", "cc", "dd", "ee"]) == {1: 1, 2: 4}

def test_bin_len_edge_case_empty_list() -> None:
    """Test with empty input list."""
    assert bin_len([]) == {}

def test_invert_keyerror_on_duplicate_value() -> None:
    """Raises KeyError if duplicate values exist in original dictionary."""
    with pytest.raises(KeyError):
        invert({'kris': 'jordan', 'michael': 'jordan'})
