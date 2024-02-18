# BUBBLE SORT

# time complexity: O(n^2)
# space complexity: O(1)

# quick video: https://www.youtube.com/watch?v=xli_FI7CuzA

# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
# works between every 2 elements, from left to right, if the left is greater than the right, swap them
# nexted for loop
# first loop is to loop through the array
# second loop is to loop through the array again, to compare the elements

# largest number bubbles to the end of the array, which is why inner loop iterates n - 1 - i times


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:

                arr[j+1], arr[j] = arr[j], arr[j+1]
                # arr[j + 1] = arr[j]
                # arr[j] = arr[j+1]

    return arr


print(bubble_sort([2, 3, 5, 1]))
