import sys

input = sys.stdin.readline
cnt = [0, 0]

for _ in range(10):
    n = int(input())

    if n % 3 == 0:
        cnt[0] = cnt[0] + 1
    if n % 5 == 0:
        cnt[1] = cnt[1] + 1

print(" ".join(map(str, cnt)))
