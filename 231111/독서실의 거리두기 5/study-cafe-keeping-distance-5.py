n = int(input())

sen = input()

seats = []
for i in range(len(sen)):
    if sen[i] == "1":
        seats.append(i)

ans = 0
for i in range(n):
    dis = n
    for seat in seats:
        dis = min(dis, abs(seat - i))
    ans = max(ans, dis)

print(ans)