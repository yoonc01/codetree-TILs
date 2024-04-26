import sys

input = sys.stdin.readline

n = int(input())

G = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    G[i][i] = 1

possible = [[0 for _ in range(n)] for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if G[i][k] and G[k][j]:
                possible[i][j] = 1

for i in range(n):
    print(" ".join(map(str, possible[i])))