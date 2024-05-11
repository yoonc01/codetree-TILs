l = list(map(int, input().split()))
l.sort()

print(l[0], l[1], l[6] - l[0] - l[1])