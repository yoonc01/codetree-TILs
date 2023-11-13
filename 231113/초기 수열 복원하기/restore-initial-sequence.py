n = int(input())
l = list(map(int, input().split()))

ans = []
for i in range(1, l[0]):
    find = True
    ans.append(i)
    for k in l:
        add = k - ans[-1]
        if add in ans or add <= 0:
            find = False
            break
        ans.append(add)
    if find:
        print(" ".join(map(str, ans)))
        break
    else:
        while(ans):
            ans.pop()
        continue