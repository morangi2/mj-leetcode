
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    k = 0  # tracks the position of the last unique element

    for i in range(1, len(nums)):
        if nums[k] != nums[i]:
            k += 1
            nums[k] = nums[i]

    return nums[:k+1]


# [1, 2, 3, 4, 5, 6]
print(removeDuplicates([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]))

# the above is a 2-pointer technique that efficiently removes duplicates, in-place, from a sorted array


def checkIfDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    k = 0  # tracks the position of the last unique element

    for i in range(1, len(nums)):
        if nums[k] != nums[i]:
            k += 1
            nums[k] = nums[i]
        else:
            return True

    return False


print(checkIfDuplicates([1, 2, 3, 4, 5, 6]))  # True
