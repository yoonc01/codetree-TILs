def getSquareTotal(n):
    if n < 10:
        return n * n
    digit = n % 10
    return getSquareTotal(n // 10) + digit * digit

n = int(input())

print(getSquareTotal(n))