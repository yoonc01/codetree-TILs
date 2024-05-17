import sys

input = sys.stdin.readline

n = int(input())

l = []

for _ in range(n):
    l.append(tuple(map(int, input().split())))

l.sort(lambda x : x[1])

ans = 0
end_time = -1

for s, e in l:
    if end_time <= s:
        end_time = e
        ans = ans + 1
print(ans)