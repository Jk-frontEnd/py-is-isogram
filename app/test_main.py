import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("", True),  # empty string
    ("playgrounds", True),  # don't repeat
    ("look", False),  # repeated and placed close
    ("abracadabra", False),  # repeated,but don"t stand close
    ("Unique", False)  # capitalized and lowercase letters
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
