import sys

input = sys.stdin.readline

directions = {"E": 0, "S": 1, "W": 2, "N": 3}

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

n = int(input())

x, y = 0, 0

for _ in range(n):
    direction, cnt = input().split()
    direction = directions[direction]
    cnt = int(cnt)

    for i in range(cnt):
        x = x + dxs[direction]
        y = y + dys[direction]

print(x, y)



