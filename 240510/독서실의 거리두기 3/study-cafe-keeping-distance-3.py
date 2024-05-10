n = int(input())
sen = input()

before = 0
dist = 0

for i in range(n):
    if sen[i] == "1":
        if i - before > dist:
            dist = i - before
        before = i

print(dist // 2)