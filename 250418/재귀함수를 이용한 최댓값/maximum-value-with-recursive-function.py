n = int(input())
arr = list(map(int, input().split()))

def max_value(i):
    if i == n - 1:
        return arr[i]
    return max(max_value(i + 1), arr[i])

print(max_value(0))