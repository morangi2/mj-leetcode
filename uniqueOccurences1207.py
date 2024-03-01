"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""


def uniqueOccurrences(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """

    seen = {}  # key == num, val == no of occurences
    uniq = {}  # key == no of occurences, val == num

    for num in arr:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1

    for freshOccurence in seen.values():
        if freshOccurence in uniq:
            return False
        else:
            uniq[freshOccurence] = 1

    return True


print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))  # True
print(uniqueOccurrences([1, 2]))  # False
print(uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))  # True
