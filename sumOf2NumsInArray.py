def twoSumBruteForce(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(twoSumBruteForce([11, 15, 2, 7], 9))  # [0, 1]


def twoSumOptimized(nums, target):
    nums_dict = {}
    for num, i in enumerate(nums):
        compliment = target - num
        if compliment in nums_dict:
            return [nums_dict[compliment], i]
        else:
            nums_dict[num] = i


print(twoSumBruteForce([11, 15, 2, 7], 9))  # [0, 1]
