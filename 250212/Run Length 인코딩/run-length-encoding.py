import sys

input = sys.stdin.readline

string = input().strip()
n = len(string)

idx = 0
result = []

while idx < n:
    char = string[idx]
    count = 0

    while idx < n and string[idx] == char:
        idx += 1
        count += 1

    result.append(char + str(count))

compressed_string = "".join(result)

print(len(compressed_string))
print(compressed_string)
