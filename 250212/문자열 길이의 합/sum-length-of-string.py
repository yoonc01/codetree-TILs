import sys

input = sys.stdin.readline

n = int(input())

ans = 0
countStartsWithA = 0

for _ in range(n):
    string = input().strip()
    if (string[0] == 'a'):
        countStartsWithA = countStartsWithA + 1
    ans = ans + len(string)

print(ans, countStartsWithA)