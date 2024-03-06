def binarySearch(data, k):
    if not data:
        return -1

    left_pointer = 0
    right_pointer = len(data) - 1

    while left_pointer <= right_pointer:
        mid_pointer = (left_pointer + right_pointer) // 2

        if data[mid_pointer] == k:
            return mid_pointer

        elif data[mid_pointer] < k:
            left_pointer = mid_pointer + 1

        elif data[mid_pointer] > k:
            right_pointer = mid_pointer - 1

    return -1

# COMPLEXITY: O(log n) time complexity because the search space is halved at each iteration
# O(1) space complexity because we are not using any extra space


# Test cases
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 5
print(binarySearch(data, k))  # 4

k = 10
print(binarySearch(data, k))  # -1

k = 1
print(binarySearch(data, k))  # 0
