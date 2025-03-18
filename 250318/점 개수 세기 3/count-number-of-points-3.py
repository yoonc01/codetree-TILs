import sys

input = sys.stdin.readline

n, q = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

def find_idx(number):
    low = 0
    ans = 0
    high = len(l) - 1
    mid = (low + high) // 2
    while(low <= high):
        if (l[mid] <= number):
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
        mid = (low + high) // 2
    return ans

for _ in range(q):
    a, b = map(int, input().split())
    print(find_idx(b) - find_idx(a) + 1)