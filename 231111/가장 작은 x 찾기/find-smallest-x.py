import sys

input = sys.stdin.readline

n = int(input())

range_info = []

for _ in range(n):
    range_info.append(list(map(int, input().split())))

for x in range(range_info[0][1] + 1):
    data = x
    possible = True
    for a, b in range_info:
        data = 2 * data
        if a <= data <= b:
            continue
        else:
            possible = False
            break
    if possible:
        print(x)
        break