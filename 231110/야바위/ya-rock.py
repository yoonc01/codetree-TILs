import sys

input = sys.stdin.readline

n = int(input())

info = []
for _ in range(n):
    info.append(list(map(int, input().split())))

ans = 0
for i in range(1, 4):
    stone = i
    score = 0
    for a, b, c in info:
        if stone == a:
            stone = b
        elif stone == b:
            stone = a
        
        if stone == c:
            score = score + 1
    ans = max(ans, score)
print(ans)