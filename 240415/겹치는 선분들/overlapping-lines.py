import sys

input = sys.stdin.readline

n, k = map(int, input().split())

end_point = 0
l = []

for _ in range(n):
    move, direction = input().split()
    move = int(move)
    if direction == "R":
        s = end_point
        e = end_point + move
        end_point = e
    else:
        s = end_point - move
        e = end_point
        end_point = s
    
    l.append((s, 1))
    l.append((e, -1))

l.sort()
over_lap = 0
first_over = 1

ans = 0

for point, v in l:
    over_lap = over_lap + v
    if over_lap >= k and first_over:
        start = point
        first_over = 0
    elif over_lap < k and not first_over:
        end = point
        first_over = 1
        ans = ans + end - start
print(ans)