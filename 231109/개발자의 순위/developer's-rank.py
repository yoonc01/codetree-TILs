import sys

input = sys.stdin.readline

n, k = map(int, input().split())

l = []

for _ in range(n):
    l.append(list(map(int, input().split())))

cnt = 0
for i in range(1, k + 1):
    for j in range(1, k + 1):
        condition = 1
        if i == j:
            continue
        for score in l:
            if score.index(i) > score.index(j):
                condition = 0
                break
        if condition:
            cnt = cnt + 1
print(cnt)