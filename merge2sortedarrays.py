def mergeSortedArray(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # define pointers for nums1 and nums2 and for the list to be returned i.e. nums1
    # compare the last elements of nums1 and nums2 and add the greater to the end of nums1
    # decrement the pointer of the list that had the greater element
    # repeat the process until all elements of nums2 are added to nums1
    # if there are still elements in nums1, add them to the beginning of nums1
    # return nums1

    pointer = len(nums1) - 1
    m -= 1
    n -= 1

    while m >= 0 and n >= 0:
        if nums1[m] >= nums2[n]:  # if the last element of nums1 is greater than the last element of nums2
            # add the last element of nums1 to the end of nums1
            nums1[pointer] = nums1[m]
            m -= 1
        else:
            # add the last element of nums2 to the end of nums1
            nums1[pointer] = nums2[n]
            n -= 1
        # decrement the pointer
        pointer -= 1

    return nums1


# [1, 2, 2, 3, 5, 6]
print(mergeSortedArray([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))


def mergeSortedArray2(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: List[int]
    """
    merged = []
    pointer1 = 0
    pointer2 = 0

    while pointer1 < m and pointer2 < n:
        if nums1[pointer1] <= nums2[pointer2]:
            merged.append(nums1[pointer1])
            pointer1 += 1
        else:
            merged.append(nums2[pointer2])
            pointer2 += 1

    while pointer1 < m:
        merged.append(nums1[pointer1])
        pointer1 += 1

    while pointer2 < n:
        merged.append(nums2[pointer2])
        pointer2 += 1

    return merged


# [1, 2, 2, 3, 5, 6]
print(mergeSortedArray2([1, 2, 3], 3, [2, 5, 6], 3))
