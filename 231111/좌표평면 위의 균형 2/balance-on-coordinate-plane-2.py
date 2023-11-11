import sys

input = sys.stdin.readline

n = int(input())

points = []
for _ in range(n):
    points.append(list(map(int, input().split())))

ans = sys.maxsize
for i in range(0, 101, 2):
    for j in range(0, 101, 2):
        one = 0
        two = 0
        three = 0
        four = 0
        for x, y in points:
            if i < x and j < y:
                one = one + 1
            elif x < i and j < y:
                two = two + 1
            elif x < i and y < j:
                three = three + 1
            elif i < x and y < j:
                four = four + 1
        max_val = max(one, two, three, four)
        ans = min(ans, max_val)
print(ans)