"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""

# PSEUDOCODE
"""
- n pairs of parentheses so n*2 total parentheses == total length of the string
- vars:
    - left, right, to rep: ( and ) and start from zero
    - empty string to store the current string
    - result [] to store the valid combinations
    - stack of tuples to store the current string and the left and right parentheses
- loop from 0 to n*2
    - pop the top tuple in the stack ..
        - gives you the current string and the left and right parentheses count
    - if len(s) == 2n, then append the string to result
    - if left < n,
        - append a new tuple to stack; concatenate ( to s and increment the val of left by 1
            - eg stack.append((left + 1, right, s + '(' ))
    - if right < left,
        - append a new tuple to stack; concatenate ) to s and increment the val of right by 1
            - eg stack.append((left, right + 1, s + ')' ))
- return result

Time complexity: O(4^n / sqrt(n)) because we have 2n total parentheses and we have 2 choices for each parentheses
Space complexity: O(4^n / sqrt(n)) because we have 2n total parentheses and we have 2 choices for each parentheses

"""


def generateParenthesis(n):
    left, right = 0, 0
    result = []
    s = ''
    # stack of tuples to store the current string and the left and right parentheses
    stack = [(left, right, s)]

    while stack:
        left, right, s = stack.pop()

        if len(s) == n * 2:  # if the length of the string is equal to 2n because we have n pairs of parentheses
            result.append(s)

        if left < n:  # start with left to make it valid parenthesis
            stack.append((left + 1, right, s + '('))

        if right < left:  # needs to catch up with left to make it valid
            stack.append((left, right + 1, s + ')'))

        print(stack)

    return result


print(generateParenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]
