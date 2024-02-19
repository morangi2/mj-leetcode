# ILLUSTRATION: https://www.youtube.com/watch?v=MK-NZ4hN7rs
# PSEUDOCODE
"""
Q: SMALLEST sub-array with a given sum == DYNAMIC sliding window
    smallest == minimize something
    sub-array == contiguous OR sequential
    condition == >= sum
>
    in: array, input_sum
    variables: 
        start_window_index (since this will be changing dynamically in the loop)
        sub_array_size (since we are trying to minimize the sub-array size) initialized to infinity
        current_window_sum (since we are trying to calculate the sum of the sub-array)
    condition: sum of current_window_sum >= input_sum
    out: sub_array_size

    - loop through array
        - start_window_index = 0
        - window_end == the for loop tracker, i.e. i
        - keep adding to current_window_sum
        - check: current_window_sum >= input_sum ?
            - yes:
                - iterate through the array and keep shrinking the left hand side of the window while the condition is still true
                - ask if the window size can get smaller, can I do better, aka keep shrinking the left hand side of the window
                    - get the min sub_array_size
                    - update the current_window_sum by subtracting the value at the start_window_index
                    - increment the start_window_index towards the right
            - no:
                - continue looping
"""


import math

s = {"m": 1, "e": 1}
spec = s.get("m")
print(spec)


def smallestSubArraySum(arr, input_sum):
    start_window = 0
    # == infinity i.e. the largest possible number so initialize to this, since we are trying to minimize the sub-array size
    min_window_size = math.inf
    current_window_sum = 0

    for i in range(len(arr)):
        current_window_sum += arr[i]
        if current_window_sum >= input_sum:
            # ask if the window size can get smaller, can I do better, aka keep shrinking the left hand side of the window
            while (current_window_sum >= input_sum):
                min_window_size = min(min_window_size, i - start_window + 1)
                current_window_sum -= arr[start_window]
                start_window += 1

    if min_window_size == math.inf:
        return 0

    return min_window_size


print(smallestSubArraySum([4, 2, 2, 7, 8, 1, 2, 8, 10], 8))  # 1
print(smallestSubArraySum([4, 2, 2, 7, 8, 1, 2, 8, 10], 100))  # 0
print(smallestSubArraySum([4, 2, 2, 7, 8, 1, 2, 8, 10], 10))  # 1
print(smallestSubArraySum([4, 2, 2, 7, 8, 1, 2, 8, 10], 12))  # 2
