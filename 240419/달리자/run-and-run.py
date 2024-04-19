n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

move = []
for i in range(n):
    move.append(a[i] - b[i])

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if move[j] < 0:
            if move[i] + move[j] > 0:
                move[i] = move[i] + move[j]
                ans = ans + -move[j] * (j - i)
            if move[i] + move[j] <= 0:
                ans = ans + move[i] * (j - i)
                move[i] = 0
                break
                
print(ans)