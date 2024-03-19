# not complete
def lastVisitedIntegers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    seen = []
    ans = []
    k = 0
    
    for i in range(len(nums)):
        if nums[i] > 0:
            seen.insert(0, nums[i])
            print("seen: ")
            print(seen)
        elif nums[i] == -1:
            if nums[i-1] != -1:
                print("previous num is: ", nums[i-1])
                k = 1
            else:
                k += 1
                if k <= len(seen):
                    ans.append(seen[k-1])
                elif k > len(seen):
                    ans.append(nums[i])
                
                print("k: ")
                print(k)

                print("ans: ")
                print(ans)

    return ans


# nums1 = [1,2,-1,-1,-1]
# print(lastVisitedIntegers(nums1))  # [2,1,-1]

nums2 = [1,-1,2,-1,-1]
print(lastVisitedIntegers(nums2))  # [1,2,1]