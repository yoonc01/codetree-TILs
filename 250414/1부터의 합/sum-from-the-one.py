n = int(input())

total = 0
for i in range(1, 101):
    total = total + i
    if (total >= N):
        print(i)
        break
