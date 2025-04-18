import sys

input = sys.stdin.readline

G1 = [list(map(int, input().split())) for _ in range(3)]
input()
G2 = [list(map(int, input().split())) for _ in range(3)]


for i in range(3):
    for j in range(3):
        print(G1[i][j] * G2[i][j], end = " ")
    print()
