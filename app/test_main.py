import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("AaA", False),
    ("", True),
    ("love", True),
    ("abracadabra", True),
    ("a a chanel the fire", False),
    ("abcd", True),
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
