def until_one(n):
    if (n == 1):
        return 0
    if (n % 2 == 0):
        return until_one(n // 2) + 1
    return until_one(n // 3) + 1

n = int(input())

print(until_one(n))