import math


def maxSumSubArrayNoWindowSize(arr):
    # given an array of both positive and negative integers, get the maximum sum of any subarray of size 1 or more
    # in: int array
    # out: int. maximum Sum of the subarray of size 1 or more

    # pseudo-code:
    """

        var: max_sum, current_sum
        loop from 0 to n
            current_sum = max(arr[i], current_sum + arr[i])
            max_sum = max(max_sum, current_sum)
        return max_sum

    """

    n = len(arr)
    max_sum = math.inf * -1  # == - infinity i.e. the smallest possible number
    current_sum = 0

    for i in range(n):
        current_sum += arr[i]
        max_sum = max(max_sum, current_sum)

        if max_sum > current_sum:
            current_sum = arr[i]

    return max_sum


# test cases
print(maxSumSubArrayNoWindowSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 55
print(maxSumSubArrayNoWindowSize([-1, 2, 3, -4, 5, 6, 7, 8, 9, 10]))  # 45

# smaller array with negative numbers and positive numbers
print(maxSumSubArrayNoWindowSize([-1, 2, 6, 3, -4, 5, 6]))  # 11
