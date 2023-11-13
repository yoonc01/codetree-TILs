import sys

input = sys.stdin.readline

d = {}
n, k = map(int, input().split())
for i in range(n):
    bomb = int(input())

    if bomb in d:
        d[bomb].append(i)
    else:
        d[bomb] = [i]

max_val = 0
ans = 0
bombs = list(d.keys())
bombs.sort()
for bomb in bombs:
    cnt = 0
    for i in range(len(d[bomb]) - 1):
        if d[bomb][i + 1] - d[bomb][i] <= k:
            cnt = cnt + 1
    if cnt != 0 and max_val <= cnt:
        max_val = cnt
        ans = bomb
print(ans)