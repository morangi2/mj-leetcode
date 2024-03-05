def findInMonotonic(matrix, k):
    # - monotonic matrix is a matrix where all the elements are in increasing order
    # - i.e. each row and each column is sorted in increasing order
    # PSEUDOCODE
    """
    - start at the bottom left corner
    - if k is greater than the current element, move right
    - if k is less than the current element, move up
    """

    rows = len(matrix) - 1
    cols = 0

    # edge case
    if not matrix or not matrix[0]:
        return False

    while rows >= 0 and cols < len(matrix[0]) - 1:
        curr_val = matrix[rows][cols]

        if curr_val == k:
            return True
        elif curr_val < k:  # advance to the right of the same col
            cols += 1
        elif curr_val > k:  # advance to the row above in the same col
            rows -= 1

    return False


# test cases
a = [[0, 0, 0, 1], [1, 1, 3, 2], [2, 3, 4, 5]]  # false
b = [[0, 0, 0, 1], [1, 1, 1, 2], [2, 3, 4, 5]]  # true

print(findInMonotonic(a, 7))
print(findInMonotonic(b, 1))
