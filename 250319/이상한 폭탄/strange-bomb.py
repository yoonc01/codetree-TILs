n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

d = {}
ans = -1

for idx, num in enumerate(arr):
    if num in d and idx - d[num] <= k:
        ans = max(ans, num)
    d[num] = idx

print(ans)
