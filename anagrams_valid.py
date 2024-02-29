def isAnagram(s, t):
    """
    PSEUDOCODE:
    - sort s
    - sort t
    - if equal, return True
    """

    s = ''.join(sorted(s))
    t = "".join(sorted(t))
    is_anagram = False
    print(s)
    print(t)

    if s == t:
        is_anagram = True

    return is_anagram


print(isAnagram("anagram", "nagaram"))
