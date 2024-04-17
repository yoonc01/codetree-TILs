s = int(input())

left = 1
right = s

ans = 1
while (left <= right):
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 <= s:
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1
print(ans)