# 2개의 마을 + 간선 유지비용 최소 = 최소신장트리 이후 비용 최대노드 제거
from collections import deque

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
edge = []
total_cost = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    # a to b의 비용 c
    edge.append((c, a, b))

edge.sort()
max_cost = 0

# 최소 신장 트리
for e in edge:
    cost, a, b = e
    # 사이클 안 생기면 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        total_cost += cost
        max_cost = cost

print(total_cost - max_cost)
