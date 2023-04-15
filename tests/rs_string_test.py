from unittest import TestCase
import rs_string


class RsStringTestCase(TestCase):
    def test_is_empty(self):
        self.assertTrue(rs_string.is_none_or_empty(""))
        self.assertFalse(rs_string.is_none_or_empty(" "))

    def test_is_none_or_empty(self):
        self.assertTrue(rs_string.is_none_or_empty(None))
        self.assertTrue(rs_string.is_none_or_empty(""))
        self.assertFalse(rs_string.is_none_or_empty(" "))

    def test_is_whitespace(self):
        self.assertTrue(rs_string.is_whitespace(" "))
        self.assertTrue(rs_string.is_whitespace("\t"))
        self.assertTrue(rs_string.is_whitespace("\n"))
        self.assertTrue(rs_string.is_whitespace("\r"))
        self.assertTrue(rs_string.is_whitespace("\f"))
        self.assertTrue(rs_string.is_whitespace("\v"))
        self.assertFalse(rs_string.is_whitespace(""))

    def test_is_none_whitespace(self):
        self.assertTrue(rs_string.is_none_or_whitespace(None))
        self.assertTrue(rs_string.is_none_or_whitespace(""))
        self.assertTrue(rs_string.is_none_or_whitespace(" "))
        