import unittest

from utils.luhn import _digits_of, _luhn_checksum, is_luhn_valid


class LuhnTest(unittest.TestCase):
    def test_digits_of(self):
        self.assertEqual(_digits_of('123456789'), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_luhn_checksum(self):
        self.assertEqual(_luhn_checksum('123456789'), 7)
        self.assertEqual(_luhn_checksum('022043850'), 5)
        self.assertEqual(_luhn_checksum('957392048'), 2)
        self.assertEqual(_luhn_checksum('304859302'), 3)

    def test_is_luhn_valid(self):
        self.assertFalse(is_luhn_valid('123456789'))
        self.assertFalse(is_luhn_valid('022043850'))
        self.assertFalse(is_luhn_valid('957392048'))
        self.assertFalse(is_luhn_valid('304859302'))
        self.assertTrue(is_luhn_valid('4111111111111111'))
        self.assertTrue(is_luhn_valid('5454545454545454'))
