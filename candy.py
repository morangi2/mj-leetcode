
def candy(ratings):
    n = len(ratings)
    candies = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    for i in range(n-3, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i+1] + 1)

    return sum(candies)


print(candy([1, 0, 2]))  # 5
print(candy([1, 2, 2]))  # 4
print(candy([1, 2, 3, 4, 5]))  # 15
print(candy([10, 2, 4, 2, 6, 1, 7, 8, 9, 2, 1]))  # 26

# The time complexity is O(n) and the space complexity is O(n).

# problem statement:
"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""
