import sys

input = sys.stdin.readline

n, m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def in_range(a, b):
    return (0 <= a < n and 0 <= b < m)

def square(x, y):
    cnt = 0
    for i in range(x, x + 2):
        for j in range(y, y + 2):
            if in_range(i, j):
                cnt = cnt + G[i][j]
    return cnt

def max_triangle(x, y):
    global ans
    square_area = square(x, y)
    for i in range(x, x + 2):
        for j in range(y, y + 2):
            if in_range(i, j):
                ans = max(ans, square_area - G[i][j])

def max_line(x, y):
    global ans
    cnt = 0
    for i in range(x, x + 3):
        if in_range(i, y):
            cnt = cnt + G[i][y]
    ans = max(ans, cnt)
    cnt = 0
    for j in range(y, y + 3):
        if in_range(x, j):
            cnt = cnt + G[x][j]
    ans = max(ans, cnt)

for i in range(n):
    for j in range(m):
        max_triangle(i, j)
        max_line(i, j)

print(ans)
    