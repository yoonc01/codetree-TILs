n, k = map(int, input().split())

l = [int(input()) for _ in range(n)]

l = l[::-1]

cnt = 0
for i in l:
    cnt = cnt + k // i
    k = k % i

print(cnt)