# this is a N^2 algorithm but it is faster than bubble sort and selection sort
# illustration: https://www.geeksforgeeks.org/insertion-sort/
# Time complexity: O(n^2) - quadratic
# Space complexity: O(1) - constant

# works from current index to the left, swap the values in while loop and swap the key at the end/outside of the loop


# insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands
# it is efficient for small data sets, much like other quadratic sorting algorithms
# it is more efficient in practice than most other simple quadratic algorithms such as bubble sort and selection sort
# it is adaptive, that means it reduces its total number of steps if a partially sorted array is provided as input
# it is stable, that means it does not change the relative order of elements with equal keys
# it is in-place, that means it requires a constant amount of additional memory space
# it is online, that means it can sort a list as it receives it


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):  # loop through the array
        key = arr[i]  # store the key in a variable
        j = i - 1  # let j loop through the array, starting from element on the left of the key
        """ 
        # loop through the array from the key to the beginning, i is the outer boundary to prevent IndexOutOfRange error
        while j >= 0 and arr[j] > key:
            # keep moving elements to the right and decrement j and swap the 2 current values, until the condition is false
            arr[j+1] = arr[j]
            arr[j] = key
            j -= 1
        """

        # ALTERNATIVE
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr


print(insertion_sort([4, 3, 2, 10, 12, 1, 5, 6]))
