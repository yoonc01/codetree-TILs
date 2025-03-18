import sys

input = sys.stdin.readline

def get_distance(check1, check2):
    x1, y1 = check1
    x2, y2 = check2
    return (abs(x2 - x1) + abs(y2 - y1))

n = int(input())

left = [0 for _ in range(n)]
right = [0 for _ in range(n)]

l = [[0, 0] for _ in range(n)]
for i in range(n):
    l[i] = list(map(int, input().split()))

for i in range(1, n):
    left[i] = left[i - 1] + get_distance(l[i], l[i - 1])
    right[n - i - 1] = right[n - i] + get_distance(l[n - i - 1], l[n - i])

ans = sys.maxsize
for i in range(1, n - 1):
    ans = min(ans, left[i - 1] + get_distance(l[i - 1], l[i + 1]) + right[i + 1])

print(ans)