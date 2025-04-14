n, m = map(int, input().split())

for i in range(n):
    print(" ".join(map(str, ["*" for _ in range(m)])))