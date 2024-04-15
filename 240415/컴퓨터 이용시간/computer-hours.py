import sys

input = sys.stdin.readline

n = int(input())

l = []

for i in range(n):
    s, e = map(int, input().split())
    l.append((s, 1, i + 1))
    l.append((e, -1, i + 1))

l.sort()

com = [0] * n

ans = []
for point, v, person in l:
    if v == 1:
        for i in range(n):
            if com[i] == 0:
                com[i] = com[i] + person
                ans.append((person, i + 1))
                break
    else:
        for i in range(n):
            if com[i] == person:
                com[i] = 0
                break

ans.sort()

for person, i in ans:
    print(i, end = " ")