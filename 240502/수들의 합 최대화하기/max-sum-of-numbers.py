import sys

input = sys.stdin.readline

n = int(input())

G = [list(map(int, input().split())) for _ in range(n)]
col_visited = [False] * n

ans = 0

def backtrack(i, total):
    global ans
    if i == n:
        ans = max(ans, total)
        return
    
    for j in range(n):
        if not col_visited[j]:
            col_visited[j] = True
            backtrack(i + 1, total + G[i][j])
            col_visited[j] = False

backtrack(0, 0)

print(ans)