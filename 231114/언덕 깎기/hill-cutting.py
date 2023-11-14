import sys

input = sys.stdin.readline

n = int(input())

h = []

min_val = sys.maxsize
max_val = 0
for _ in range(n):
    height = int(input())
    min_val = min(min_val, height)
    max_val = max(max_val, height)
    h.append(height)

ans = sys.maxsize
for x in range(84):
    min_cost = 0
    for hill in h:
        if x <= hill <= x + 17:
            continue
        elif hill < x:
            min_cost = min_cost + (x-hill)**2
        else:
            min_cost = min_cost + (hill - x - 17)**2
    ans = min(ans, min_cost)
print(ans)