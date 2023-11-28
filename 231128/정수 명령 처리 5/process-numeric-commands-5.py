n = int(input())

l = []

for _ in range(n):
    cmd = list(input().split())
    if cmd[0] == "push_back":
        l.append(cmd[1])
    elif cmd[0] == "pop_back":
        l.pop()
    elif cmd[0] == "size":
        print(len(l))
    elif cmd[0] == "get":
        print(l[int(cmd[1]) - 1])