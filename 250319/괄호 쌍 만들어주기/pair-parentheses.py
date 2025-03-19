string = input()


cnt_closed = 0

for i in range(len(string) - 1):
    if (string[i] == ")" and string[i + 1] == ")"):
        cnt_closed = cnt_closed + 1

ans = 0

for i in range(len(string) - 1):
    if (string[i] == "(" and string[i + 1] == "("):
        ans = ans + cnt_closed
    elif (string[i] == ")" and string[i + 1] == ")"):
        cnt_closed = cnt_closed - 1

print(ans)
        