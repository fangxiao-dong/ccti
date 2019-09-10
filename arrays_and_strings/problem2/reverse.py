class Solution(object):
    """"Implement a function to reverse a null terminated string"""

    def reverse(self, str):
        res = ''
        for c in str:
            res = c + res

        return res
