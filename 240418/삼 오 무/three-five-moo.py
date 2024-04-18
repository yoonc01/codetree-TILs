n = int(input())

ans = 6 * (n // 3)

if n % 3 == 0:
    print(ans - 2)
elif n % 3 == 1:
    print(ans + 1)
else:
    print(ans + 2)