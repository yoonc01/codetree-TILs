n = int(input())

l = list(map(int, input()))

def cal(seats):
    n = len(seats)
    dis = n
    for i in range(n):
        for j in range(i + 1, n):
            dis = min(dis, abs(seats[j] - seats[i]))
    return dis
seats = []
for i in range(n):
    if l[i] == 1:
        seats.append(i)

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        dis = n
        if i in seats or j in seats:
            continue
        seats.append(i)
        seats.append(j)
        ans = max(ans,cal(seats))
        seats.pop()
        seats.pop()
print(ans)