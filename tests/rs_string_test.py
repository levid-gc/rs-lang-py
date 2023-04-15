import pytest
from src import rs_string


@pytest.mark.parametrize(["value", "expected"], [("", True), (" ", False)])
def test_is_empty(value, expected):
    assert rs_string.is_none_or_empty(value) is expected


@pytest.mark.parametrize(["value", "expected"], [(None, True), ("", True), (" ", False)])
def test_is_none_or_empty(value, expected):
    assert rs_string.is_none_or_empty(value) is expected


@pytest.mark.parametrize(["value", "expected"], [
    (" ", True), ("\t", True), ("\n", True),
    ("\r", True), ("\f", True), ("\v", True),
    ("", False),
])
def test_is_whitespace(value, expected):
    assert rs_string.is_whitespace(value) is expected


@pytest.mark.parametrize(["value", "expected"], [(None, True), ("", True), (" ", True)])
def test_is_none_whitespace(value, expected):
    assert rs_string.is_none_or_whitespace(value) is expected
        