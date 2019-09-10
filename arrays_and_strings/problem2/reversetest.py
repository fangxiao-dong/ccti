import unittest
from reverse import Solution

class TestReverse(unittest.TestCase):

    def test_no_char(self):
        self.assertEqual(Solution().reverse(''), '')

    def test_one_char(self):
        self.assertEqual(Solution().reverse('a'), 'a')

    def test_normal(self):
        self.assertEqual(Solution().reverse('abc'), 'cba')

if __name__ == '__main__':
    unittest.main(verbosity=2)