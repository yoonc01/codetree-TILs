import sys

input = sys.stdin.readline

def condition(l1, l2, l3, lines):
    counts = [0 for i in range(101)]
    for i in range(len(lines)):
        if i in [l1, l2, l3]:
            continue
        a, b = lines[i]
        for j in range(a, b + 1):
            counts[j] = counts[j] + 1
            if counts[j] >= 2:
                return False
    return True
        
    

n = int(input())

lines = [list(map(int, input().split())) for i in range(n)]

cnt = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j  + 1, n):
            if condition(i, j, k, lines):
                cnt = cnt + 1
print(cnt)