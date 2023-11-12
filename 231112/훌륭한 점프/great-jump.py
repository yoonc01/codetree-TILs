n, k = map(int, input().split())
l = list(map(int, input().split()))

def possible(max_val):
    count = []
    for i in range(n):
        if l[i] <= max_val:
            count.append(i)
    for i in range(len(count) - 1):
        if count[i + 1] - count[i] > k:
            return False
    return True

ans = max(l) + 1
for max_val in range(max(l[0], l[-1]), max(l) + 1):
    if possible(max_val):
        ans = min(ans, max_val)
print(ans)