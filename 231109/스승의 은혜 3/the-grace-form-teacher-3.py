import sys

input = sys.stdin.readline

def cal_sum(info):
    total = 0
    for i in info:
        total = total + sum(i)
    return total

n, b = map(int, input().split())

info = [list(map(int, input().split())) for i in range(n)]

ans = 0

for i in range(n):
    total = 0
    for j in range(n):
        if j == i:
            total = total + sum(info[j]) - info[j][0] // 2
        else:
            total = total + sum(info[j])
        if total > b:
            ans = max(ans, j)

print(ans)