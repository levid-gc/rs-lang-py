import re


def is_empty(value):
    return value == ""


def is_none_or_empty(value):
    return value is None or is_empty(value)


def is_whitespace(value):
    '''
    :param value: Space, tab, line feed(newline), carriage return, form feed, vertical tab
    :return: True or False
    '''
    return re.match(r"^\s+$", value) is not None


def is_none_or_whitespace(value):
    return is_none_or_empty(value) or is_whitespace(value)
