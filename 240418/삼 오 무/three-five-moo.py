n = int(input())

ans = 15 * (n // 8)

if n % 8 == 0:
    print(ans - 1)
elif n % 8 == 1:
    print(ans + 1)
elif n % 8 == 2:
    print(ans + 2)
elif n % 8 == 3:
    print(ans + 4)
elif n % 8 == 4:
    print(ans + 7)
elif n % 8 == 5:
    print(ans + 8)
elif n % 8 == 6:
    print(ans + 11)
elif n % 8 == 7:
    print(ans + 13)