def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    k = 2

    for i in range(2, len(nums)):
        if nums[i] != nums[k-2]:
            nums[k] = nums[i]
            k += 1

    return k


print(removeDuplicates([1, 1, 1, 2, 2, 3]))  # 5

# the above is a 2-pointer technique that efficiently removes duplicates, in-place, after they occur twice, from a sorted array
