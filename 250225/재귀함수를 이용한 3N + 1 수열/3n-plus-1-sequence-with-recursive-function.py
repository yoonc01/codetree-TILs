def count(n):
    if (n == 1):
        return 0;
    if (n % 2 == 0):
        return count(n // 2) + 1;
    return count(3 * n + 1) + 1;

n = int(input())

print(count(n))
