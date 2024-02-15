
def minRemovedParenthesis(s):
    stack = []
    count_valid = 0
    invalid = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if stack:
                stack.pop()
                count_valid += 1  # count the number of valid parenthesis
            else:
                s = s[:i] + s[i+1:]  # remove the invalid parenthesis
                invalid += 1       # count the number of invalid parenthesis

    return (f"valid sentence: {s}, no. of invalid parenthesis: {invalid} and no. of valid parenthesis: {count_valid}")


print(minRemovedParenthesis("lee(t(c)o)de)"))  # lee(t(c)o)de, 1
