import unittest
from compress import Solution

class TestCompress(unittest.TestCase):

    def tests(self):
        self.assertEqual(Solution().compress(''), '' )
        self.assertEqual(Solution().compress('aabbccdefff'), 'aabbccdefff')
        self.assertEqual(Solution().compress('abc'), 'abc')
        self.assertEqual(Solution().compress('aabbcccccddee'), 'a2b2c5d2e2')

if __name__ == '__main__':
    unittest.main(verbosity=2)