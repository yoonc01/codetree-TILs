import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    total = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            total = total + i
    print(total)