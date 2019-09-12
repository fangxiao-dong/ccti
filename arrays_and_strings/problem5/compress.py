class Solution(object):
    """Implement a method to perform basic string compression using the counts of repeated characters."""

    def compress(self, tstr):
        if len(tstr) == 0:
            return ''

        result = ''
        repeatCount = 1
        last = tstr[0]

        for i in range(1, len(tstr)):
            if tstr[i] == last:
                repeatCount += 1
            else:
                result += last + str(repeatCount)
                repeatCount = 1
                last = tstr[i]

        # String concatenation is not very efficient as it creates new copy of strings every iteration. Better to use list to append and ''.join.
        result += last + str(repeatCount)

        if len(tstr) <= len(result):
            return tstr
        else:
            return result
 
