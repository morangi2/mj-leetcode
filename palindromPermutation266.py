def canPermutePalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    # put is in a Counter
    # this returns a dict with the count of each char
    # if the length of the string is even, all the chars must be even
    # if the length of the string is odd, only one char can be odd
    # loop through the dict and count the odd chars
    # if the count is more than 1, return False
    # else return True

    """
    from collections import Counter
    count = Counter(s)
    print(count)  # Counter({'a': 2, 'r': 2, 'c': 2, 'e': 1})
    odd = 0
    for i in count:
        if count[i] % 2 != 0:
            odd += 1
    return odd <= 1

    """

    # OR

    n = len(s)
    my_dict = {}

    for c in s:
        if c in my_dict:
            my_dict[c] += 1
            if my_dict[c] > 2:
                return False
        else:
            my_dict[c] = 1

    count = 0

    for i in my_dict:
        if my_dict[i] % 2 != 0:  # if the count is odd
            count += 1

    return count <= 1


print(canPermutePalindrome("carerac"))
