import sys

input = sys.stdin.readline

while (True):
    s = input().strip()
    if (s == "END"):
        break
    print(s[::-1])