n, m, k = map(int, input().split())

dist = list(map(int, input().split()))

horse = [0] * n
ans = 0
def backtrack(num):
    global ans

    total = 0
    for i in horse:
        if i >= m:
            total = total + 1
    ans = max(ans, total)
    
    if num == n:
        return

    for i in range(k):
        if horse[i] >= m:
            continue
        horse[i] = horse[i] + dist[num]
        backtrack(num + 1)
        horse[i] = horse[i] - dist[num]

backtrack(0)
print(ans)