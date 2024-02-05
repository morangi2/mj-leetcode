def binarySearch(nums, target):
    left_pointer = 0
    right_pointer = len(nums) - 1

    while left_pointer <= right_pointer:
        mid = (left_pointer + right_pointer) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left_pointer = mid + 1
        else:
            right_pointer = mid - 1

    return -1

# the above is a binary search algorithm that searches for a target in a sorted array
# first, we define the left and right pointers
# then we calulate the mid-point
# if the mid-point is the target, immediately return the mid-point
# if the mid point is less that the tartget, adjust the left pointer to mid + 1
# if the mid point is greater than the target, adjust the right pointer to mid - 1
# if the target is not found, return -1


print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))  # 4
print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))  # -1
