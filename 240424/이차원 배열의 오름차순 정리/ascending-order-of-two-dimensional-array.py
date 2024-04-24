def mid_idx(mid, l, k):
    cnt = 1
    for i in l:
        if i < mid:
            cnt = cnt + 1
        else:
            if cnt <= k:
                return True
    return False
n = int(input())

k = int(input())

l = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        l.append(i * j)
l.sort()
left = 1
right = n * n
ans = right

while(left <= right):
    mid = (left + right) // 2
    if mid_idx(mid, l, k):
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
print(ans)