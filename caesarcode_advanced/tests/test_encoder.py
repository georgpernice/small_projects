"""Test encoder.py."""

import unittest
from caesarcode_advanced.encoder import Encoder


class TestEncoder(unittest.TestCase):
    """Test methods of Encoder class."""

    def setUp(self) -> None:
        self.encoder = Encoder()

    def test_encode_is_reversible(self: "unittest.Testcase"):
        """Apply decode on encoded string. Expect them to cancel out each other."""
        teststring = "hi I am desmond."
        encoded_string = self.encoder.encode(teststring)
        assert teststring == self.encoder.decode(encoded_string)

    def test_encode_letter_substitutions(self: "unittest.Testcase"):
        """See if letters are substituted correctly for a few ones."""
        # permut_circle1 = "aeiou "
        # permut_circle2 = "bcdfghjklmnpqrstvwxyz"
        cleartext = "hell oh"
        expected = "jimmauj"
        assert self.encoder.encode(cleartext) == expected

    def test_untouched_symbols(self: "unittest.Testcase"):
        """See if untouched symbols like "." and "!" are not touched like expected for a few of them."""
        cleartext = ",.!)()<>"
        assert self.encoder.encode(cleartext) == cleartext
