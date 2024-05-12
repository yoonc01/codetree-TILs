def is_possible(mid, n):
    if (mid + 1) * mid // 2 <= n:
        return True
    return False

n = int(input())

left = 0
right = n
ans = 0

while(left <= right):
    mid = (left + right) // 2
    if is_possible(mid, n):
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1
print(ans)