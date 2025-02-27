n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

belt = l + r + d

def move(arr):
    temp = arr[3 * n - 1]
    for i in range(3 * n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = temp

t = t % (3 * n)

for _ in range(t):
    move(belt)

print(" ".join(map(str, belt[:n])))
print(" ".join(map(str, belt[n:2*n])))
print(" ".join(map(str, belt[2*n:])))
