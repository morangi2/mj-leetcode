def mergeSort(nums):
    # PSEUDOCODE
    # ILLUSTRATION: https://www.youtube.com/watch?v=jlHkDBEumP0
    """
        - check for edge cases; if length of nums is <= 1 i.e. empty or of size 1
        - mergeSort(nums)
            - define upper, lower and mid bounds
            - split the array into 2 (leftArray, rightArray), demarcated by mid
            - recursively call mergeSort on the 2 split arrays
            - call a merge function on the 3 arrays, subArray1, subArray2, and nums
        - merge(subArray1, subArray2, nums)
            - define the lower bounds for all 3 arrays; i, j, k = 0, 0, 0
            - loop through both arrays
                - while(i < len(subArray1) and j < len(subArray2)):
                    - compare values at current positions
                        - smaller val is put into nums
                        - increment its pointer
                        - increment k

                - check to see if 1 of the 2 arrays is still untouched, and continue looping in its values
                    - if i >= len(subArray1)  == then subArray2 is likely not empty
                        while j < len(subArray2):
                            append values of subArray2 to nums
                        - and inverse
    """

    def merge(leftArray, rightArray, resultArray):
        i, j, k = 0, 0, 0

        while (i < len(leftArray) and j < len(rightArray)):
            if leftArray[i] < rightArray[j]:
                resultArray[k] = leftArray[i]
                i += 1
                k += 1
            else:
                resultArray[k] = rightArray[j]
                j += 1
                k += 1

        if i >= len(leftArray):
            while (j < len(rightArray)):
                resultArray[k] = rightArray[j]
                j += 1
                k += 1
        if j >= len(rightArray):
            while (i < len(leftArray)):
                resultArray[k] = leftArray[i]
                i += 1
                k += 1

    n = len(nums)

    if n <= 1:
        return nums

    lower = 0
    upper = n
    mid = (lower + upper) // 2

    left = nums[:mid]
    right = nums[mid:]

    mergeSort(left)
    mergeSort(right)
    merge(left, right, nums)

    return nums


# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mergeSort([3, 2, 1, 5, 4, 6, 7, 8, 9, 10]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mergeSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mergeSort([10, 1, 9, 2, 8, 3, 7, 4, 6, 5]))
