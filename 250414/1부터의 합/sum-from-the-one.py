n = int(input())

total = 0
for i in range(1, 101):
    total = total + i
    if (total >= n):
        print(i)
        break
