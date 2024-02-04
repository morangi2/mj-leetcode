def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    occ = 2

    for i in range(2, len(nums)):
        if nums[i] != nums[occ-2]:
            nums[occ] = nums[i]
            occ += 1

    return occ


print(removeDuplicates([1, 1, 1, 2, 2, 3]))  # 5
