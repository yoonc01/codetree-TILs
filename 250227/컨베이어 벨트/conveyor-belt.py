n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

belt = u + d

t = t % (2 * n)

def move(l):
    temp = l[2 * n - 1]
    for i in range(2 * n - 1, 0, -1):
        l[i] = l[i - 1]
    l[0] = temp

for _ in range(t):
    move(belt)

print(" ".join(map(str, belt[:n])))
print(" ".join(map(str, belt[n:])))
