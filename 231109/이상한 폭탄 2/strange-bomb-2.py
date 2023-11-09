import sys

input = sys.stdin.readline

def in_range(idx, l):
    return (idx < l)

n, k = map(int, input().split())

bombs = []
for _ in range(n):
    bombs.append(int(input()))

ans = -1
for i in range(n):
    pivot = bombs[i]
    for j in range(1, k + 1):
        if in_range(i + j, n) and pivot == bombs[i + j]:
            ans = max(ans, pivot)
print(ans)