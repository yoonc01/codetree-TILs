def check_arr(l, check):
    for a, b in zip(l, check):
        if a != b:
            return False
    return True

l = list(map(int, input().split()))
l.sort()

max_val = max(l[:8]) + 1
for a in range(1, max_val):
    for b in range(a, max_val):
        for c in range(b, max_val):
            for d in range(c, max_val):
                check = [a, b, c, d, a + b, b + c, c + d, d + a, a + c, b + d, a + b + c, a + b + d, a + c + d, b + c + d, a + b + c + d]
                check.sort()
                if check_arr(l, check):
                    print(a, b, c, d)
                    exit()