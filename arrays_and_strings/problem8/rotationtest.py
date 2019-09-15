import unittest
from rotation import Solution

class TestRotatin(unittest.TestCase):

    def tests(self):
        self.assertTrue(Solution().isrotation('waterbottle', 'bottlewater'))
        self.assertFalse(Solution().isrotation('waterbottle', 'bottleswater'))
        self.assertTrue(Solution().isrotation('', ''))
        self.assertFalse(Solution().isrotation('waterbottle', 'Bottlewater'))

if __name__ == '__main__':
    unittest.main(verbosity=2)