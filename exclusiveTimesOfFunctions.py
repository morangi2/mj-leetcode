def exclusiveTime(n, logs):
    """
    :type n: int
    :type logs: List[str]
    :rtype: List[int]
    """
    stack = []
    response = [0] * n

    for log in logs:
        fId, func, curr_time = log.split(":")

        fId, curr_time = int(fId), int(curr_time)

        if func == "start":
            stack.append((fId, curr_time))
        elif func == "end" and fId == stack[-1][0]:
            fn_id, insert_time = stack.pop()
            time_taken = curr_time - insert_time + 1
            response[fn_id] += time_taken

            if stack:
                response[stack[-1][0]] -= time_taken

    return response


# [3, 4]
print(exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))

# code explanation:
# 1. create a stack and a response list of size n
# 2. iterate through the logs
# 3. split the log into the function id, the function name and the current time
# 4. if the function name is "start", push the function id and the current time to the stack
# 5. if the function name is "end" and the function id is the same as the last function id in the stack
# 6. pop the last function id and the insert time from the stack
# 7. calculate the time taken by subtracting the current time from the insert time and adding 1
# 8. add the time taken to the response list at the index of the function id
# 9. if the stack is not empty, subtract the time taken from the last function id in the stack
# 10. return the response list
# 11. the time complexity is O(n) and the space complexity is O(n)
