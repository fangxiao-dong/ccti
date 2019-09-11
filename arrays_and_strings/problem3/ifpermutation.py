class Solution(object):
    
    def ifpermutation(self, str1, str2):
        if not len(str1) == len(str2):
            return False

        if ''.join(sorted(str1)) == ''.join(sorted(str2)):
            return True
        else:
            return False
