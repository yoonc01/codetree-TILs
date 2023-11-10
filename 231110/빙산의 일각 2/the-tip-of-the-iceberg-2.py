n = int(input())

l = []

for _ in range(n):
    l.append(int(input()))

min_val = min(l) - 1
max_val = max(l) + 1

ans = 0

for level in range(min_val, max_val):
    cnt = 0
    count_start = 1
    for h in l:
        if h <= level:
            count_start = 1
        else:
            if count_start == 0:
                continue
            else:
                cnt = cnt + 1
                count_start = 0

    ans = max(ans, cnt)
print(ans)