import sys

input = sys.stdin.readline

n = int(input())

l = []

for i in range(n):
    s, e = map(int, input().split())
    l.append([i, s, 1])
    l.append([i, e, -1])
    

l.sort(key = lambda x : x[1])

left = set()
ans = 0
for num, s, v in l:
    if v == 1:
        if not left:
            ans = ans + 1
        left.add(num)
    else:
        left.remove(num)
    
print(ans)