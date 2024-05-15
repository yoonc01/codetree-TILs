n = int(input())

c = 65
for i in range(n):
    for j in range(i + 1):
        print(chr((c - 65) % 26 + 65), end = "")
        c = c + 1
    print()