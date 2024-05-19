from collections import deque

l = list(map(str, input()))
q = deque(l)

print("".join(map(str, q)))
for _ in range(len(l)):
    q.rotate(1)
    print("".join(map(str, q)))