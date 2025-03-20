import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()
j = n - 1
ans = 0
for i in range(n):
    while j != 0 and arr[i] + arr[j] > k:
        j = j - 1
    
    if j <= i:
        break
    ans = ans + j - i

print(ans)