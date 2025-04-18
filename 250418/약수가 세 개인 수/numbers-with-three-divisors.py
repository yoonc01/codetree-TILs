start, end = map(int, input().split())

ans = 0
for i in range(start, end + 1):
    cnt = 2
    for d in range(2, i):
        if i % d == 0:
            cnt = cnt + 1
        
    if cnt == 3:
        ans = ans + 1
print(ans)