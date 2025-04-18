G = [list(map(int, input().split())) for _ in range(4)]

ans = 0

for i in range(4):
    for j in range(4):
        if (G[i][j] % 5 == 0):
            ans = ans + 1

print(ans)