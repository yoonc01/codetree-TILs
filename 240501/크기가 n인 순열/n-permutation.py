def choose(n, visited, l, num):
    if num == 0:
        print(" ".join(map(str, l)))
        return
    

    for i in range(1, n + 1):
        if visited[i]:
            continue
        l.append(i)
        visited[i] = True
        choose(n, visited, l, num - 1)
        l.pop()
        visited[i] = False

n = int(input())

choose(n, [False] * (n + 1), [], n)