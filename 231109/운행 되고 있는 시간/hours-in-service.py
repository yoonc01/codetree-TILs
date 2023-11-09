import sys

input = sys.stdin.readline

n = int(input())

time = []
for _ in range(n):
    time.append(list(map(int, input().split())))

ans = 0

for i in range(n):
    counts = [0 for _ in range(1000)]

    for j in range(n):
        if j == i:
            continue
        a, b = time[j]

        for k in range(a, b):
            counts[k] = 1
        ans = max(ans, sum(counts))
print(ans)