import sys

input = sys.stdin.readline

def distance(x1, y1, x2, y2):
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

n = int(input())

l = []

for _ in range(n):
    l.append(list(map(int, input().split())))

ans = sys.maxsize

for i in range(n - 1):
    for j in range(i + 1, n):
        x1, y1 = l[i]
        x2, y2 = l[j]
        d = distance(x1, y1, x2, y2)
        if d < ans:
            ans = d

print(ans)