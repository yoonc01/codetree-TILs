import sys

input = sys.stdin.readline

def ceil(n):
    if n == int(n):
        return n
    else:
        return int(n) + 1
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    total = 0
    for i in range(ceil(a / 2), b // 2 + 1):
        total = total + 2 * i
    print(total)