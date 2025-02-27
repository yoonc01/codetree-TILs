import sys

input = sys.stdin.readline

n, m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def check_all_positive(x, y, w, h):
    for i in range(h):
        for j in range(w):
            if (G[x + i][y + j] <= 0):
                return False
    return True

def findMax():
    global ans

    for w in range(1, m + 1):
        for h in range(1, n + 1):
            for i in range(n - h + 1):
                for j in range(m - w + 1):
                    if (check_all_positive(i, j, w, h)):
                        ans = max(ans, w * h)

findMax()
print(ans)
