n = int(input())

def print_rect(n):
    cnt = 1
    for _ in range(n):
        line = []
        for _ in range(n):
            line.append(cnt)
            cnt = cnt % 9 + 1
        print(" ".join(map(str, line)))

print_rect(n)