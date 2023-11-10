x, y = map(int, input().split())

cnt = 0
for i in range(x, y + 1):
    sen = str(i)
    if sen == sen[::-1]:
        cnt = cnt + 1
print(cnt)