a, b, x, y = map(int, input().split())

_1 = abs(b - a)
_2 = abs(y - a) + abs(b - x)
_3 = abs(b - y) + abs(x - a)

if _1 < _2 and _1 < _3:
    print(_1)
elif _2 < _1 and _2 < _3:
    print(_2)
else:
    print(_3)