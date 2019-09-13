import unittest
from zeros import Solution

class TestZeros(unittest.TestCase):

    def tests(self):
        self.assertEqual(Solution().zeros([[],[],[]]),  [[],[],[]])
        self.assertEqual(Solution().zeros([[1,2,3],[4,0,6],[0,9,8]]), [[0,0,3],[0,0,0],[0,0,0]])
        self.assertEqual(Solution().zeros([[0,1,2,3,7],[4,5,7,0,6],[8,7,0,3,4],[9,1,2,5,3]]), [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,3]])
        self.assertEqual(Solution().zeros([[1,2,3],[4,5,6],[7,9,8]]), [[1,2,3],[4,5,6],[7,9,8]])

if __name__ == '__main__':
    unittest.main(verbosity=2)