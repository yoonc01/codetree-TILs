n = int(input())

sen = input()

for length in range(1, n + 1):
    exist = False
    for start in range(n + 1 - length):
        check = sen[start: start + length]

        if check in sen[start + 1:]:
            exist = True
            break
    if not exist:
        print(length)
        break