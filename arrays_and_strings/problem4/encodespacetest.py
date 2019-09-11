import unittest
from encodespace import Solution

class TestPermutation(unittest.TestCase):

    def tests(self):
        self.assertEqual(Solution().encodeSpace('a b c d  '), 'a%20b%20c%20d' )
        self.assertEqual(Solution().encodeSpace(' abcd'), 'abcd')
        self.assertEqual(Solution().encodeSpace('a b'), 'a%20b')
        self.assertEqual(Solution().encodeSpace(''), '')

if __name__ == '__main__':
    unittest.main(verbosity=2)