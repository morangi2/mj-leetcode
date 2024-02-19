# SLIDING WINDOW PATTERN
# Suitable for iterating over a list or array in a linear fashion i.e. sequentially = contigous sequence of elements
# The window can be a subarray of a given size or a subarray of a given condition
# strings, arrays, linked lists, trees, graphs, etc can be iterated in a contigous sequence i.e. a linear fashion
# HINT: if you are trying to find the min, max, longest, shortest, if it contains X, subarray of a given size or condition, then sliding window pattern is the best approach
# when you need to calculate something

# QUESTION VARIANTS:
# FIXED LENGTH
# 1. Find the maximum sum of a subarray of a given size
# 2. Find the minimum sum of a subarray of a given size
# 3. Find the longest subarray of a given size
# 4. Find the shortest subarray of a given size
# 5. Find the subarray that contains a given value
# 6. Find the subarray that does not contain a given value
# 7. Find the subarray that contains a given condition
# 8. Find the subarray that does not contain a given condition

# DYNAMIC LENGTH
# smallest sum >= to some value S
# longest subarray with sum <= to some value S
# longest subarray with sum >= to some value S
# longest subarray with sum == to some value S
# longest subarray with sum != to some value S


# Dynamic Length with Auxilliary Data Structure, meaning that the data structure is used to store the sum of the subarray
# smallest sum >= to some value S
# longest subarray with sum <= to some value S
# longest subarray with sum >= to some value S
# longest subarray with sum == to some value S
# longest subarray with sum != to some value S

# String PERMUTATIONS
# Find the longest subarray with distinct characters eg does string2 exist as a subarray in string1


import math


def maxSumSubArray(arr, k):
    # in: int array, int window size
    # in every loop: sum subarray of size k
    # out: int. maximum Sum of the subarray of size 3

    # pseudo-code:
    """

        var: max_sum, window_size
        loop from n:n-3
            sum index 0, 1, 2
                compare sum and max_sum
                    if sum > max_sum
                        store sum in max_sum variable
            sum index 1, 2, 3
                compare sum and max_sum
                    if sum > max_sum
                        store sum in max_sum variable
            ...
            ...
        return max_sum

    """

    n = len(arr)
    max_sum = math.inf * -1  # == - infinity i.e. the smallest possible number
    window_size = k
    current_sum = 0

    # for i in range(0, n - window_size):
    #     current_sum = arr[i] + arr[i + 1] + arr[i + 2]

    #     if current_sum > max_sum:
    #         max_sum = current_sum

    # return max_sum

    # ALTERNATIVE
    for i in range(n):
        current_sum += arr[i]
        if (i >= window_size - 1):  # i.e. when the window size is reached
            max_sum = max(max_sum, current_sum)
            # subtract the value of the first element from the current window
            # subtract before you loop to the next item in the arr cz then the next loop will have 1 unneeded value in the window
            current_sum = current_sum - arr[i - (window_size - 1)]  

    return max_sum


print(maxSumSubArray([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3))  # 16
print(maxSumSubArray([4, 2, 1, 7, 8, 1, 2, 8, 1, 0, 3], 3))  # 19
