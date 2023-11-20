import sys

input = sys.stdin.readline

l = [-1 for i in range(11)]

n = int(input())
cnt = 0
for _ in range(n):
    num, place = map(int, input().split())
    if l[num] == -1:
        l[num] = place
    else:
        if l[num] != place:
            cnt = cnt + 1
            l[num] = place
print(cnt)