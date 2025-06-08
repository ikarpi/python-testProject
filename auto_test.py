import pytest
from index import count_vowels

def test_only_vowels():
    assert count_vowels('aeiouAEIOU') == 10

def test_no_vowels():
    assert count_vowels('bcdfgBCDFG') == 0

def test_mixed_string():
    assert count_vowels('Hello World!') == 3
    assert count_vowels('Python is FUN') == 3