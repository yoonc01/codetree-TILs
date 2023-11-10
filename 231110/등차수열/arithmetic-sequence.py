n = int(input())

l = list(map(int, input().split()))

min_val = min(l)
max_val = max(l)
ans = 0
for k in range(min_val, max_val):
    cnt = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if l[i] + l[j] == 2 * k:
                cnt = cnt + 1
    
    ans = max(ans, cnt)
print(ans)