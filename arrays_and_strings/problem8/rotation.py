class Solution(object):
    """Given two strings s1 and s2, check if one word is a rotation of another word using at most one isSubstring call"""

    def isrotation(self, str1, str2):
        if not len(str1) == len(str2):
            return False

        def isSubstring(s1, s2):
            return s1 in s2

        return isSubstring(str2, str1 + str1)
        