def lengthOfLongestSubString(s):
    seen = {}  # key: char, val:last appear index seen[char] = index
    longest = 0
    start_window = 0
    n = len(s)

    for i in range(n):
        index = seen.get(s[i])

        if index is not None and index >= start_window:
            # calculate length of current substring
            current_length = i - start_window
            # every time we find a repetition we set the starting point to the character next to the last occurrence.
            start_window = index + 1

            if current_length > longest:
                longest = current_length

        seen[s[i]] = i

    if longest == 0:
        return n

    return max(longest, (n - start_window))


print(lengthOfLongestSubString("abcabcbb"))  # 3
print(lengthOfLongestSubString("pwwkew"))  # 3
print(lengthOfLongestSubString("abba"))  # 2
print(lengthOfLongestSubString(" "))  # 1
print(lengthOfLongestSubString("aab"))  # 2
