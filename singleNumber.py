class Solution(object):
    def uniqueNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Using the XOR operator
        # XOR of a number with itself is 0
        # XOR of a number with 0 is the number itself
        # XOR is commutative and associative
        # So, the result of XOR of all elements in the list will be the unique number
        # Time complexity: O(n)
        # Space complexity: O(1)

        result = 0
        for num in nums:
            result = result ^ num
            print(result)
        return result

    print(uniqueNumber([4, 1, 2, 1, 2, 5, 5]))

    # to run use: python3 singleNumber.py
