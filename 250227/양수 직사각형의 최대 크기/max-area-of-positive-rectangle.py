import sys

input = sys.stdin.readline

n, m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
ans = -1

def check_all_positive(x1, x2, y1, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if (G[i][j] <= 0):
                return False
    return True

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                if (check_all_positive(i, k, j, l)):
                    ans = max(ans, (k - i + 1) * (l - j + 1))

print(ans)