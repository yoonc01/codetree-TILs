n = int(input())

l = list(map(int, input().split()))


for i in range(n):
    for j in range(n - 1):
        if (l[j] > l[j + 1]):
            temp = l[j]
            l[j] = l[j + 1]
            l[j + 1] = temp

for i in range(n):
    print(l[i], end = " ")