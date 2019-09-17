import unittest
from rotate90 import Solution

class TestRotatin(unittest.TestCase):

    def tests(self):
        self.assertEqual(Solution().rotate([[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6]]), [[3,9,5,1],[4,0,6,2],[5,1,7,3],[6,2,8,4]])
        self.assertEqual(Solution().rotate([[1,1],[1,1]]), [[1,1],[1,1]])
        self.assertEqual(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]), [[7,4,1],[8,5,2],[9,6,3]])

if __name__ == '__main__':
    unittest.main(verbosity=2)