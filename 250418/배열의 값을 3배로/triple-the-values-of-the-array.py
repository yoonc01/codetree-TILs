import sys

input = sys.stdin.readline

G = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        print(3 * G[i][j], end = " ")
    print()