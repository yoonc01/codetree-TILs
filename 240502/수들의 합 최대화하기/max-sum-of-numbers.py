import sys

input = sys.stdin.readline

n = int(input())

G = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

def is_possible(a, b):
    for i in range(n):
        if visited[a][i] or visited[i][b]:
            return False
    return True

ans = 0

def backtrack(l, num):
    global ans
    if num == 0:
        total = 0
        for a, b in l:
            total = total + G[a][b]
        ans = max(ans, total)
        return
    
    for i in range(n):
        for j in range(n):
            if not is_possible(i, j):
                continue
            visited[i][j] = True
            l.append((i, j))
            backtrack(l, num - 1)
            l.pop()
            visited[i][j] = False

backtrack([], n)

print(ans)