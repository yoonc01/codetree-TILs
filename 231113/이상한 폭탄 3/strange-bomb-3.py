import sys

input = sys.stdin.readline

n, k = map(int, input().split())

bombs = []
min_num = sys.maxsize
max_num = 0
for _ in range(n):
    bomb = int(input())
    min_num = min(min_num, bomb)
    max_num = max(max_num, bomb)
    bombs.append(bomb)

ans = 0
for num in range(min_num, max_num + 1):
    first = True
    cnt = 0
    for idx, bomb in enumerate(bombs):
        if bomb == num:
            if first:
                first = False
            else:
                if idx - pre <= k:
                    cnt = cnt + 1
                    ans = max(ans, cnt)
                else:
                    cnt = 0
            pre = idx
print(ans)