import re


def is_empty(value) -> bool:
    if type(value) == str:
        return value == ""
    return False


def is_none_or_empty(value) -> bool:
    return value is None or is_empty(value)


def is_whitespace(value) -> bool:
    """
    :param value: Space, tab, line feed(newline), carriage return, form feed, vertical tab
    """
    return re.match(r"^\s+$", value) is not None


def is_none_or_whitespace(value) -> bool:
    return is_none_or_empty(value) or is_whitespace(value)
