import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

numberSet = set()
j = -1
ans = 0
for i in range(n):
    while(j + 1 < n and arr[j + 1] not in numberSet):
        numberSet.add(arr[j + 1])
        j = j + 1
    ans = max(ans, j - i + 1)
    numberSet.remove(arr[i])

print(ans)

