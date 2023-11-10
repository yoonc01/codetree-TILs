def condition(sen):
    l = []
    for i in sen:
        if i in l:
            continue
        else:
            l.append(i)
            if len(l) >= 3:
                return False
    if len(l) == 1:
        return False
    return True

x, y = map(int, input().split())

ans = 0
for i in range(x, y + 1):
    if condition(str(i)):
        ans = ans + 1

print(ans)