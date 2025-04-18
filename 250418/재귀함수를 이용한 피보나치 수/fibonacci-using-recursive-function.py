def fab(n):
    if n == 1 or n == 2:
        return 1
    return fab(n - 1) + fab(n - 2)

n = int(input())

print(fab(n))
