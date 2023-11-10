def condition(sen):
    d = {}
    for i in sen:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    if len(d) == 2 and 1 in d.values():
        return True
    return False

x, y = map(int, input().split())

ans = 0
for i in range(x, y + 1):
    if condition(str(i)):
        ans = ans + 1

print(ans)