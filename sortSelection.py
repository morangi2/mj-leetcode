# SELECTION SORT

# time complexity: O(n^2)
# space complexity: O(1)
# In-place: Yes
# Selection sort is a simple sorting algorithm. This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts, the sorted part at the left end and the unsorted part at the right end.
# Initially, the sorted part is empty and the unsorted part is the entire list.
# The smallest element is selected from the unsorted array and swapped with the leftmost element, and that element becomes a part of the sorted array.
# This process continues moving unsorted array boundary by one element to the right.

# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.
# The algorithm maintains two subarrays in a given array.
# 1. The subarray which is already sorted.
# 2. Remaining subarray which is unsorted.
# In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.
# Following example explains the above steps:

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        temp_min_val = arr[i]

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # update the index in the loop and update the values at the end/outside of the loop

        """        
        # swap the values
        arr[i] = arr[min_index]
        arr[min_index] = temp_min_val 
        """

        if (i != min_index):
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print(selection_sort([4, 3, 2, 10, 12, 1, 5, 6]))
