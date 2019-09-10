import unittest
from uniqchar import UniqueChar

class TestUniqueChar(unittest.TestCase):

    def test_onechar(self):
        self.assertTrue(UniqueChar.isUnique('a'))

    def test_nochar(self):
        self.assertTrue(UniqueChar.isUnique(''))

    def test_over256(self):
        self.assertFalse(UniqueChar.isUnique('a' * 257))

    def test_normal_positive(self):
        self.assertTrue(UniqueChar.isUnique('abcdefg'))

    def test_normal_negative(self):
        self.assertTrue(UniqueChar.isUnique('abbccdeft'))

    def test_wrong_type(self):
        self.assertRaises(TypeError, UniqueChar.isUnique, 123)

if __name__ == '__main__':
    unittest.main(verbosity=2)