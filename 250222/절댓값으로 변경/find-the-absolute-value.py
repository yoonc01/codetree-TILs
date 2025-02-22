def array_abs(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

n = int(input())
arr = list(map(int, input().split()))
array_abs(arr)
print(" ".join(map(str, arr)))