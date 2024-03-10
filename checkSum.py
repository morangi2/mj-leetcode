"""
Intuit  1st round....

given a table (eg below), get the diff between the max and the min on each row
then return the sum of all the rows' differences....

# input is a string, with \n as a seperater
input = "5 7 8 9
8 7 6
4 5 6"
"""


def checkSumDiffThenTotal(input):
    result = 0
    input = input.split("\n")

    for row in input:
        row = row.split()
        row = sorted(row)
        low = row[0]
        low_int = int(low)
        high = row[-1]
        high_int = int(high)
        diff = high_int - low_int

        result += diff

    return result


input1 = "5 7 8 9 \n 8 7 6 \n 4 5 6"

print(checkSumDiffThenTotal(input1))  # 8
