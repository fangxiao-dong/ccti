import unittest
from removeduplicate import Solution
import sys, os

# This only works when running this as module: i.e, python -m
# from ..helpers.linkedlist import Node

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
from linkedlist import Node

class RemoveDuplicateTest(unittest.TestCase):

    def setUp(self):
        """Create a test linked list"""

        myllhead = Node(1)
        myllhead.append(2)
        myllhead.append(2)
        myllhead.append(3)
        myllhead.append(3)

        self.myllhead = myllhead

    def tests(self):
        Solution().removeduplicate(self.myllhead)
        self.assertEqual(self.myllhead.data, 1)
        self.assertEqual(self.myllhead.next.data, 2)
        self.assertEqual(self.myllhead.next.next.data, 3)
        self.assertIsNone(self.myllhead.next.next.next)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
