n, s = map(int, input().split())
arr = list(map(int, input().split()))

j = 0
ans = n
sum_val = 0
for i in range(n):
    while(j < n and sum_val < s):
        sum_val = sum_val + arr[j]
        j = j + 1
    
    if (sum_val >= s):
        ans = min(ans, j - i)
    sum_val = sum_val - arr[i]

print(ans if ans != n else -1)