"""
Prompt
A Toeplitz Matrix is one where the values on every diagonal are the same: Given a 2d matrix (multidimensional array), return true if the input is a Toeplitz matrix and false otherwise.

 

Example of a valid Toeplitz matrix:

1 2 3 4
5 1 2 3
6 5 1 2
7 6 5 1

"""


def isToeplitz(m):
    # your code here
    """
    PSEUDOCODE:
    - create a for loop that will traverse the matrix... len(m) will give the number of rows in the matrix
    - create an inner for loop that will traverse the matrix... len(m[i]) will give the number of elements in the current row
    - if the current element is not equal to the element at the top left of the current element, return False
    - return True
    """
    for i in range(1, len(m)):
        for j in range(1, len(m[i])):
            if (m[i][j] != m[i-1][j-1]):
                return False

    return True


matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [6, 5, 1, 2], [7, 6, 5, 1]]

print(isToeplitz(matrix))
