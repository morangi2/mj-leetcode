"""
Criteo round 2

given a string of parenthesis determine if it has valid pairs of parenthesis, and 
return true or false

eg "((" false

"()()()" true

"""


def validParenthesis(input):
    n = len(input)
    count_open = 0

    # edge case:
    if n <= 1:
        return False

    for p in input:
        if p == "(":
            count_open += 1
        else:
            if count_open < 1:  # no opening bracket has been added
                return False
            else:  # reduce by one to cancel out the closing bracket
                count_open -= 1

    return count_open == 0


input1 = "()()()"
print(validParenthesis(input1))  # True

input2 = "((()))"
print(validParenthesis(input2))  # True

input3 = "(((((()"
print(validParenthesis(input3))  # False
