def traverse(matrix):
    output = []

    for i in range(len(matrix)):
        print("i:", matrix[i])
        for j in range(len(matrix) - 1, -1, -1):
            # check position of j first (-2) to get the row, then i (0) to get the column
            output.append(matrix[j][i])
            print("output: ", output)

    return output


# [7, 4, 1, 8, 5, 2, 9, 6, 3]
print(traverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# read the row first, then the column
