n = int(input())

arr = list(map(int, input().split()))

ans = [0 for _ in range(n)]

for i, number in enumerate(arr):
    ans[i] = number ** 2

print(" ".join(map(str, ans)))