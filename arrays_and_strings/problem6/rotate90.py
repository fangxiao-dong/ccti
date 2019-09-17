class Solution(object):
    """Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degree."""

    def rotate(self, matrix):
        nrow = len(matrix)
        nlayer = nrow / 2

        for layer in range(nlayer):
            last = nrow - 1 - layer
            for index in range(layer, last):
                top = matrix[layer][index]

                matrix[layer][index] = matrix[last - index + layer][layer]
                matrix[last - index + layer][layer] = matrix[last][last - index + layer]
                matrix[last][last - index + layer] = matrix[index][last]
                matrix[index][last] = top

        return matrix

