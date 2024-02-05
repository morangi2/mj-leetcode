# brute force solution to count the number of elements in a list that are greater than a target number
# optimize the solution to use a binary search algorithm

def countNumbersGreaterThanTarget(nums, target):
    count = 0
    for num in nums:
        if num > target:
            count += 1

    return count


print(countNumbersGreaterThanTarget([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))  # 4
