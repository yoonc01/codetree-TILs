n = int(input())

even = []

arr = list(map(int, input().split()))

for i in arr:
    if i % 2 == 0:
        even.append(i)

print(" ".join(map(str, even[::-1])))