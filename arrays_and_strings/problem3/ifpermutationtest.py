import unittest
from ifpermutation import Solution

class TestPermutation(unittest.TestCase):

    def tests(self):
        self.assertFalse(Solution().ifpermutation('a' * 3, 'a' * 2))
        self.assertTrue(Solution().ifpermutation('Hello', 'eolHl'))
        self.assertFalse(Solution().ifpermutation('Hello', 'eoLHl'))
        self.assertTrue(Solution().ifpermutation('', ''))

if __name__ == '__main__':
    unittest.main(verbosity=2)