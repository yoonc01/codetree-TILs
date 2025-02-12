import sys

input = sys.stdin.readline

strings = input().split()

ans = 0

for string in strings:
    ans = ans + len(string)

print(ans)