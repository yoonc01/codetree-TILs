import sys

input = sys.stdin.readline

G = [input().rstrip() for _ in range(3)]

check = []
ans = 0
for line in G:
    l = list(set(line))
    l.sort()
    if len(l) == 2:
        if l not in check:
            ans = ans + 1
        check.append(l)    
for i in range(3):
    l = []
    for j in range(3):
        l.append(G[j][i])
        l = list(set(l))
        l.sort()
    if len(l) == 2:
        if l not in check:
            ans = ans + 1
        check.append(l)    
        
l = []
l.append(G[0][0])
l.append(G[1][1])
l.append(G[2][2])
l = list(set(l))

if len(l) == 2:
    if l not in check:
        ans = ans + 1
    check.append(l)   


l = []
l.append(G[0][2])
l.append(G[1][1])
l.append(G[2][0])
l = list(set(l))

if len(l) == 2:
    if l not in check:
        ans = ans + 1
    check.append(l)   

print(ans)