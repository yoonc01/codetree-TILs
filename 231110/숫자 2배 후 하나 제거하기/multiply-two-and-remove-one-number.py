import sys

input = sys.stdin.readline
n = int(input())

l = list(map(int, input().split()))

ans = sys.maxsize

for i in range(n):
    l[i] = 2 * l[i]
    for j in range(n):
        remained_arr = [elem for k, elem in enumerate(l) if k != j]

        sum_diff = 0
        for k in range(n - 2):
            sum_diff = sum_diff + abs(remained_arr[k + 1] - remained_arr[k])
        ans = min(sum_diff, ans)
    l[i] = l[i] // 2
print(ans)