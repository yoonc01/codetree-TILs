import sys

def swap(string, a, b):
    a, b = int(a) - 1, int(b) - 1
    str_list = list(string)  
    str_list[a], str_list[b] = str_list[b], str_list[a]
    return "".join(str_list)

def change(string, a, b):
    return string.replace(a, b)

s, q = sys.stdin.readline().split()
q = int(q)

for _ in range(q):
    cmd, a, b = sys.stdin.readline().split()

    if cmd == "1":
        s = swap(s, a, b)
    else:
        s = change(s, a, b)

    print(s)
