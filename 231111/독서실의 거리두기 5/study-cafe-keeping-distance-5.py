n = int(input())

sen = input()

seats = []
for i in range(len(sen)):
    if sen[i] == "1":
        seats.append(i)

ans = 0
for i in range(n):
    dis = n
    check = False
    for seat in seats:
        if i in seats:
            continue
        dis = min(dis, abs(seat - i))
        check = True
    if check:
        ans = max(ans, dis)

print(ans)