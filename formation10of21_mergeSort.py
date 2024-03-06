
"""
PSEUDOCODE:
- break down the arr into the smallest vals, then merge
- get the mid index
    - left_pointer = 0
    - right_pointer = len(arr) -1
    - mid == floor division of the 2
- create 2 arrays demarcated by mid pointer
- recursively call merge sort on both arrays
- call merge on the 2 arrays
- merge function...
    - takes in 3 arrays (if sorting in place):
        - left array, right array, and result array
    - get starting indexes of all 3, i, j, k== 0
    - loop while i < len(arr_left) and j < len(arr_right):
        - check which value is smaller,
            - append to result_array
            - increment position of that array
            - increment position of result_array
    - return result_array
- return input array
"""


def mergeSort(data):

    def merge(left_arr, right_arr, arr):
        i, j, k = 0, 0, 0

        while (i < len(left_arr) and j < len(right_arr)):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1

        # check to see if either of the 2 arrays still has values left and append them to arr

        if i >= len(left_arr):
            while (j < len(right_arr)):
                arr[k] = right_arr[j]
                j += 1
                k += 1

        if j >= len(right_arr):
            while (i < len(left_arr)):
                arr[k] = left_arr[i]
                i += 1
                k += 1

    if len(data) <= 1:
        return data

    lower = 0
    upper = len(data)
    mid = (lower + upper) // 2

    left_array = data[:mid]
    right_array = data[mid:]

    mergeSort(left_array)
    mergeSort(right_array)
    merge(left_array, right_array, data)

    return data


print(mergeSort([3, 2, 1, 5, 4, 6, 7, 8, 9, 10]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(mergeSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# edge case
print(mergeSort([10, 1, 9, 2, 8, 3, 7, 4, 6, 5]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# edge case
print(mergeSort([1]))
# [1]

# edge case
print(mergeSort([]))
# []

# edge case
print(mergeSort([1, 2]))
# [1, 2]
