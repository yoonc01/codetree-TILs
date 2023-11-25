s = input()
find = input()

s_len = len(s)
f_len = len(find)

for i in range(s_len - f_len + 1):
    exist = True
    for j in range(f_len):
        if find[j] != s[i + j]:
            exist = False
            break
    if exist:
        print(i)
        break
    elif i == s_len - f_len and not exist:
        print(-1)