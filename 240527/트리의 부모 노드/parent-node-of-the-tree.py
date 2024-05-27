import sys

input = sys.stdin.readline


def travel(x, G, visited, parent):
    for i in G[x]:
        if not visited[i]:
            visited[i] = True
            parent[i] = x
            travel(i, G, visited, parent)

n = int(input())

G = [[] for _ in range(n)]
visited = [False for _ in range(n)]
parent = [0 for _ in range(n)]

for _ in range(n - 1):
    s, e = map(int, input().split())
    G[s - 1].append(e - 1)
    G[e - 1].append(s - 1)

travel(0, G, visited, parent)

for i in parent[1:]:
    print(i + 1)