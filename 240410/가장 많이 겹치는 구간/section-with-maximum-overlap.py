import sys

input = sys.stdin.readline

n = int(input())

points = []

for i in range(n):
    s, e = map(int, input().split())
    points.append([s, 1])
    points.append([e, -1])

max_val = -1
sum_val = 0
points.sort()
for x, v in points:
    if v == -1:
        max_val = max(max_val, sum_val)
    sum_val = sum_val + v
    max_val = max(max_val, sum_val)
    
print(max_val)