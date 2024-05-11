import sys

input = sys.stdin.readline

d = {"A": 0, "B": 0}

n = int(input())

top = ""
ans = 0
for _ in range(n):
    c, s = input().split()
    s = int(s)
    
    d[c] = d[c] + s

    if top != "A" and d["A"] > d["B"]:
        ans = ans + 1
        top = "A"
    elif top != "" and top != "A and B" and d["A"] == d["B"]:
        ans = ans + 1
        top = "A and B"
    elif top != "B" and d["B"] > d["A"]:
        ans = ans + 1
        top = "B"

print(ans)