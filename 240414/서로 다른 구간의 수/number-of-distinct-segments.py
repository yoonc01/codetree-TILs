import sys

input =  sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    s, e = map(int, input().split())
    l.append([s, 1])
    l.append([e, -1])

l.sort()
ans = 0
cnt = 0
for x, score in l:
    cnt = cnt + score
    if cnt == 1 and score == 1:
        ans = ans + 1
print(ans)