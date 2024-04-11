n, s = map(int, input().split())

l = list(map(int, input().split()))

sum_val = l[0]
j = 0
ans = n + 1
for i in range(n):
    while j + 1 < n and sum_val < s:
        sum_val = sum_val + l[j + 1]
        j = j + 1

    if sum_val < s:
        break
    if sum_val >= s:
        ans = min(ans, j - i + 1)
    sum_val = sum_val - l[i]

print(ans if ans < n + 1 else -1)