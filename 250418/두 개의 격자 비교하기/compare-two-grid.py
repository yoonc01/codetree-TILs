import sys

input = sys.stdin.readline

n, m = map(int, input().split())

G1 = [list(map(int, input().split())) for _ in range(n)]
G2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (G1[i][j] == G2[i][j]):
            print(0, end = " ")
        else:
            print(1, end = " ")
    print()