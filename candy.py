
def candy(ratings):
    n = len(ratings)
    candies = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i+1] + 1)

    return sum(candies)


print(candy([1, 0, 2]))  # 5
print(candy([1, 2, 2]))  # 4
print(candy([1, 2, 3, 4, 5]))  # 15

# The time complexity is O(n) and the space complexity is O(n).
