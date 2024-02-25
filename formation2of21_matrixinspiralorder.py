"""
Prompt
Given a 2D rectangular matrix, return all of the values in a single, linear array in spiral order. Start at (0, 0) and first include everything in the first row. Then down the last column, back the last row (in reverse), and finally up the first column before turning right and continuing into the interior of the matrix.

 

For example:

 1  2  3  4
 5  6  7  8
 9 10 11 12
 13 14 15 16

Returns:
[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
"""


def spiralTraversal(matrix):
    # your code here
    """
    PSEUDOCODE:
    - create a result list
    - create a while loop that will run until the matrix is empty
    - append the first row to the result list
    - remove the first row
    - append the last column to the result list
    - remove the last column
    - append the last row in reverse to the result list
    - remove the last row
    - append the first column in reverse to the result list
    - remove the first column
    - return the result list
    HACKS
    - matrix.pop(0) removes the first row
    - matrix.pop() removes the last row
    - row.pop() removes the last element of the row
    - row.pop(0) removes the first element of the row
    - matrix[::-1] traverses the matrix from the last row to the first row
    - matrix[0] checks if the first row is not empty
    - matrix and matrix[0] checks if there are still rows in the matrix and the first row is not empty
    - 
    """
    result = []

    if matrix is None:
        return result

    while matrix:
        result += matrix.pop(0)  # append the 1st row to the result list
        # if there are still rows in the matrix... matirx[0] checks if the first row is not empty
        if matrix and matrix[0]:
            for row in matrix:  # traverse the matrix row by row
                # append the last column to the result list... row.pop() removes the last element of the row
                result.append(row.pop())
        if matrix:  # if there are still rows in the matrix
            # append the last row in reverse to the result list... matrix.pop() removes the last row ... [::-1] reverses the row
            result += matrix.pop()[::-1]
        # if there are still rows in the matrix and the first row is not empty
        if matrix and matrix[0]:
            for row in matrix[::-1]:  # traverse the matrix from the last row to the first row
                # append the first column in reverse to the result list ... row.pop(0) removes the first element of the row
                result.append(row.pop(0))

    return result


# [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
print(spiralTraversal(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))

print(spiralTraversal([]))  # []
