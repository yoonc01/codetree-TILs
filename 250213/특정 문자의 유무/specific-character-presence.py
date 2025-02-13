import sys

input = sys.stdin.readline

string = input().strip()

ans = []

if ("ee" in string):
    ans.append("Yes")
else:
    ans.append("No")

if ("ab" in string):
    ans.append("Yes")
else:
    ans.append("No")

print(" ".join(ans))