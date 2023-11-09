import sys

input = sys.stdin.readline

def par_x(y1, y2, y3):
    return (y1 == y2 or y2 == y3 or y3 == y1)
def par_y(x1, x2, x3):
    return (x1 == x2 or x2 == x3 or x3 == x1)

def condition(x1, y1, x2, y2, x3, y3):
    return (par_x(x1, x2, x3) and par_y(y1, y2, y3))
    
n = int(input())

dots = []

for _ in range(n):
    dots.append(list(map(int, input().split())))

ans = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            x1, y1 = dots[i]
            x2, y2 = dots[j]
            x3, y3 = dots[k]

            s = abs(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3)
            if ans < s:
                ans = s
print(s)