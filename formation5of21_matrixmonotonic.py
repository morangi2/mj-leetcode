def isMonotonic(m):
    """
    PSEUDOCODE:
    - traverse all the rows... len(m)
    - traverse all the elements in each column... len(m[r])
        - compare current element to left element 
            - if current - left < 0
                - return false
    - otherwise return true
    """

    for r in range(len(m)):
        for c in range(1, len(m[r])):
            prev = m[r][c-1]
            curr = m[r][c]

            # review current row, adjacent elements
            if curr < prev:
                return False

            # review prev row after the 1st row, same col
            if r > 0:
                if curr < m[r-1][c]:
                    return False

    return True


a = [[0, 0, 0, 1], [1, 1, 3, 2], [2, 3, 4, 5]]  # false
b = [[0, 0, 0, 1], [1, 1, 1, 2], [2, 3, 4, 5]]  # true

print(isMonotonic(a))
print(isMonotonic(b))
