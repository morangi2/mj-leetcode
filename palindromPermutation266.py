def canPermutePalindrome(s):
    n = len(s)
    my_dict = {}

    for c in s:
        if c in my_dict:
            my_dict[c] += 1
            if my_dict[c] > 2:
                return False
        else:
            my_dict[c] = 1

    if n % 2 == 0:
        for i in my_dict:
            if my_dict[i] % 2 != 0:
                return False

    elif n % 2 != 0:  # can have only 1 odd char
        # keep a count of odd char
        count = 0
        if count <= 1:
            for i in my_dict:
                if my_dict[i] % 2 != 0:
                    count += 1
        else:
            return False

    return True


print(canPermutePalindrome("carerac"))
