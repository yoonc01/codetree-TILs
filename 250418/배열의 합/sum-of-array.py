import sys

input = sys.stdin.readline

for _ in range(4):
    print(sum(map(int, input().split())))