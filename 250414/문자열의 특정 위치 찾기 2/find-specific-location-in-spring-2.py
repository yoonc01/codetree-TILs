arr = ["apple", "banana", "grape", "blueberry", "orange"]

char = input()
cnt = 0

for string in arr:
    if string[2] == char or string[3] == char:
        cnt = cnt + 1
        print(string)

print(cnt)