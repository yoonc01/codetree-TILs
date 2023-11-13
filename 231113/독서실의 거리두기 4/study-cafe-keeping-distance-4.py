def min_dist(seat):
    dist = n
    for i in range(n):
        for j in range(i + 1, n):
            if seat[i] == '1' and seat[j] == '1':
                dist = min(dist, j - i)
    
    return dist

n = int(input())
seat = list(input())

ans = 0
for i in range(n):
    for j in range(i + 1, n):    
        if seat[i] == '0' and seat[j] == '0':
            seat[i] = '1'
            seat[j] = '1'
            ans = max(ans, min_dist(seat))
            seat[i] = '0'
            seat[j] = '0'

print(ans)