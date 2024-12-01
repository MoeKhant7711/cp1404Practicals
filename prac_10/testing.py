"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string `s`, `n` times, with spaces in between."""
    return " ".join([s] * n)  # Fixed to correctly pass the tests


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in.

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_phrase_to_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital letter and ending with a single full stop.

    >>> format_phrase_to_sentence("hello")
    'Hello.'
    >>> format_phrase_to_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_phrase_to_sentence("a valid phrase")
    'A valid phrase.'
    """
    phrase = phrase.strip().capitalize()  # Ensures leading/trailing spaces are removed
    if not phrase.endswith("."):
        phrase += "."  # Adds a full stop if not present
    return phrase


def run_tests():
    """Run the tests on the functions."""
    # Testing `repeat_string`
    assert repeat_string("Python", 1) == "Python", "Test failed for single repetition."
    assert repeat_string("hi", 2) == "hi hi", "Test failed for multiple repetitions."

    # Testing `Car` initialization
    # Test odometer initialization
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly."

    # Test fuel initialization with default value
    test_car = Car()
    assert test_car.fuel == 0, "Car does not set default fuel correctly."

    # Test fuel initialization with a specific value
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly when a value is provided."

    # Testing `format_phrase_to_sentence`
    assert format_phrase_to_sentence("hello") == "Hello.", "Test failed for single word."
    assert format_phrase_to_sentence("It is an ex parrot.") == "It is an ex parrot.", "Test failed for full sentence."
    assert format_phrase_to_sentence("a valid phrase") == "A valid phrase.", "Test failed for phrase without punctuation."


if __name__ == "__main__":
    # Run the custom tests
    run_tests()

    # Run doctests
    doctest.testmod()
