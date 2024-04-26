import sys

input = sys.stdin.readline

n = int(input())

G = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    G[i][i] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if G[i][k] and G[k][j]:
                G[i][j] = 1

for i in range(n):
    print(" ".join(map(str, G[i])))