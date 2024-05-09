import sys

input = sys.stdin.readline

l = list(map(int, input().split()))

l.sort()

if l[1] - 1 == l[0] and l[2] - 1 == l[1]:
    print(0)
elif l[1] - 2 == l[0] or l[2] - 2 == l[1]:
    print(1)
else:
    print(2)