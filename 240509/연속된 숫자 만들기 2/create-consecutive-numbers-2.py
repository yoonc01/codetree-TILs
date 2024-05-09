a, b, c = map(int, input().split())

if abs(a - b) == 1 and abs(b - c) == 1:
    print(0)
elif abs(a - c) == 1 and abs(b - c) == 1:
    print(0)
elif abs(b - a) == 1 and abs(c - a) == 1:
    print(0)
elif abs(a - b) == 2 or abs(b - c) == 2 or abs(c - a) == 2:
    print(1)
else:
    print(2)