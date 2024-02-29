"""
PROBLEM:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

"""
PSEUDOCODE
- create a result list
    - this will be a list of lists
- create a dict
    - key: sorted word
    - value: position of the list containing its anagrams in the res array
- loop through the input strs
    - sort one_str (and join to revert from list to a str)
    - check is the sorted one_str is in the dict:
        - if yes:
            - get the position in outer list(res) >> pos = dict[key==sorted str]
            - append to the inner list ... res[pos].append(actual_str)
        - if no:
            - append the actual_str as a list in the result list... res.append([actual_str])
            - lists append at the end so... get the len(res) -1 and add it to the dic
                - dict[key is sorted str]. values is the list position above

"""


def groupAnagrams(strs):
    res = []
    my_dict = {}

    for s in strs:
        sorted_s = ''.join(sorted(s))

        if sorted_s in my_dict:
            res_pos = my_dict[sorted_s]
            res[res_pos].append(s)
        else:
            res.append([s])
            pos = len(res) - 1
            my_dict[sorted_s] = pos

    return res


# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
