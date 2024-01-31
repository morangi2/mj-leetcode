class Solution(object):
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        half = 0
        while (x > half):
            half = half * 10 + x % 10
            x = x // 10
            print(half, x)

        if x == half or x == half // 10:
            return True

    print(isPalindrome(12321))

    # to run use: python3 palindrome.py
    # output: True
