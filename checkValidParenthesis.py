"""
Given a string containing only three types of characters: '(', ')', and '*', write a function check_valid_string(s) that checks whether the input string is valid.
The input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
A '*' can be treated as a wildcard character, which can represent either an open bracket '(' or a closing bracket ')' or nothing as well.
Write a function check_valid_string(s) that takes a string s and returns True if the string is valid, and False otherwise.

Function Signature:
def check_valid_string(s: str) -> bool:
    pass

Example:
assert check_valid_string("()") == True
assert check_valid_string("(*)") == True
assert check_valid_string("(*))") == True
assert check_valid_string("(((**)") == True
assert check_valid_string("(((*)") == False
"""

"""
def check_valid_string(s: str) -> bool:
    
    stack = []
    wild_c = []  # can be ( or ) or nothing
    result = True

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == '*':
            wild_c.append(s[i])
        elif s[i] == ')':
            stack.pop()

    if stack:
        result = False
    else:
        result = True

    return result


# print(check_valid_string("()"))
print(check_valid_string("(*)"))

"""


def check_valid_string(s: str) -> bool:
    open_bracket = 0
    close_bracket = 0
    w_card = 0

    for i in range(len(s)):
        if s[i] == '(':
            open_bracket += 1
        elif s[i] == ')':
            close_bracket += 1
        elif s[i] == '*':
            w_card += 1
    if open_bracket == close_bracket:
        return True
    elif open_bracket > close_bracket:
        compliment = open_bracket - close_bracket
        if compliment == w_card:
            return True
    elif open_bracket < close_bracket:
        compliment = close_bracket - open_bracket
        if compliment == w_card:
            return True
    return False


print(check_valid_string("()"))
print(check_valid_string("(*)"))
print(check_valid_string("(*))"))
print(check_valid_string("(((**)"))
print(check_valid_string("(((*)"))
