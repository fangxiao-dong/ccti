class UniqueChar(object):
    """Implement an algorithm to determine if a string has all unique characters. Assume given string is of ASCII nature."""

    @staticmethod
    def isUnique(str):
        """str: given string to determine if it has unique characters"""
        
        if len(str) > 256:
            return False

        hist = {}
        
        for c in str:
            if hist.get(c, 1) > 1:
                return False
        return True