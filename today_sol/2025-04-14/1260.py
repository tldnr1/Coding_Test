from collections import deque

def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    Q = deque([start])
    visited[start] = True
    
    while Q:
        v = Q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                Q.append(i)
                visited[i] = True


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# sort
for i in graph:
    i.sort()

# DFS
visited = [False] * (N + 1)
dfs(V)
print()

# BFS
visited = [False] * (N + 1)
bfs(V)