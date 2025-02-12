import sys

input = sys.stdin.readline

string = input().strip()

idx = 0
n = len(string)
result = ""
while(idx < n):
    current = string[idx]
    cnt = 0
    while (idx < n and current == string[idx]):
        idx = idx + 1
        cnt = cnt + 1
    result = result + current + str(cnt)

print(len(result))
print(result)
