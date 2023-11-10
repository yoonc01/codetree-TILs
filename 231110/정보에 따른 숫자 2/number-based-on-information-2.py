import sys

input = sys.stdin.readline

T, a, b = map(int, input().split())

d = {"S":[], "N":[]}

for _ in range(T):
    alpha, idx = input().split()
    d[alpha].append(int(idx))

cnt = 0
for i in range(a, b + 1):
    d1 = sys.maxsize
    d2 = sys.maxsize

    for j in d["S"]:
        d1 = min(d1, abs(j - i))
    for j in d["N"]:
        d2 = min(d2, abs(j - i))
    if d1 <= d2:
        cnt = cnt + 1
print(cnt)