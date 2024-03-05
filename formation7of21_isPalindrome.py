def isPalindromAnagram(word):
    """
    PSEUDOCODE
    - palindrom; spell same forwards and backwards
    - if len == even: all letters should occur 2 times only
    - if len == odd: all letters, EXCEPT 1, should occur 2 times

    ...
    - get length of word
    - var odd = 1
    - var even = 2
    - dict ; key letter, val count
        - iterate word and store letters in dict
    - iterate through the values of the dict
        - if n == even,
            if val != 2: false
        - if n == odd,
            while count >= 0:
                if val == 1; count -= 1

    """

    n = len(word)
    dict = {}
    odd = 1

    for s in word:
        if s in dict:
            dict[s] += 1
            if dict[s] > 2:
                return False
        else:
            dict[s] = 1

    for i in dict.values():
        if (n % 2 == 0):  # even word count
            if i != 2:
                return False
        elif not (n % 2 == 0):  # odd word count
            if odd > -1:
                if i == 1:
                    odd -= 1
            else:
                return False

    return True


# test cases
print(isPalindromAnagram("civic"))  # True
print(isPalindromAnagram("ivicc"))  # True
print(isPalindromAnagram("civil"))  # False
print(isPalindromAnagram("ciic"))  # True
