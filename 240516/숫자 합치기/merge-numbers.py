from collections import deque

n = int(input())

l = list(map(int, input().split()))

l.sort()

q = deque(l)
ans = 0
while(n > 1):
    a = q.popleft()
    b = q.popleft()
    ans = ans + a + b
    q.append(a + b)
    n = n - 1
print(ans)