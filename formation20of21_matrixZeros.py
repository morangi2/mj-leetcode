"""
PROMPT:
Given a rectangular matrix of numbers, find any position that is set 
to a zero in the input and then replace all values on its row and 
column with zeros. This must be done in-place, modifying the input 
matrix, not allocating any new space.

For example:

1 2 3
4 5 6
7 8 0

Becomes:

1 2 0
4 5 0
0 0 0
"""


def setMatrixZeros(matrix):
    rows = set()
    cols = set()

    print(matrix)

    # Find the positions of zeros
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)

    print(rows, cols)  # {2} {2}

    # Replace rows with zeros
    for row in rows:
        for col in range(len(matrix[row])):
            matrix[row][col] = 0

    # Replace columns with zeros
    for col in cols:
        for row in range(len(matrix)):
            matrix[row][col] = 0

    return matrix


"""
PSUEDOCODE:
- edge case; if matrix is empty, return matrix
- vars; rows, cols as sets because we don't want duplicates
- loop through the matrix
    - if matrix[row][col] == 0
        -- add row to rows
        -- add col to cols
- loop through rows
    - loop through cols
        -- matrix[row][col] = 0
- loop through cols
    - loop through rows
        -- matrix[row][col] = 0
- return matrix

Time complexity: O(n * m) where n is the number of rows and m is the number of columns in the matrix
"""


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
m2 = [[1, 2, 3], [4, 0, 6], [7, 8, 4]]

print(setMatrixZeros(m1))  # [[1, 2, 0], [4, 5, 0], [0, 0, 0]]
print(setMatrixZeros(m2))  # [[1, 0, 3], [0, 0, 0], [7, 0, 4]]
