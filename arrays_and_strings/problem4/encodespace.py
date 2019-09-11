class Solution(object):
    """Write a method to replace all spaces in a string with '%20'"""

    def encodeSpace(self, str):
        return '%20'.join(str.strip().split(' '))
