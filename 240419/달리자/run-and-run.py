n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

move = []
for i in range(n):
    move.append(a[i] - b[i])

ans = 0

for i in range(n - 1):
    if move[i] > 0:
        ans = ans + move[i]
        move[i + 1] = move[i + 1] + move[i]

print(ans)