import copy

class Solution(object):
    """Write an algorithm such that if an element in an MxN matrix is 0, it's entire row and column are set to 0"""

    def zeros(self, matrix):
        result = copy.deepcopy(matrix)
        nrows = len(matrix)
        ncolumns = len(matrix[0])

        for row in range(nrows):
            for column in range(ncolumns):
                if matrix[row][column] == 0:
                    result[row] = [0] * ncolumns
                    for row in range(nrows):
                        result[row][column] = 0
                    break
            
        return result
