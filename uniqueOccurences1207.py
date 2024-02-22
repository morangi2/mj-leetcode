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
