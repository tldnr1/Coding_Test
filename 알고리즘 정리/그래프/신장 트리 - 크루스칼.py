'''
 - 시간복잡도 : O(ElogE)

 - 비용이 적은 순서대로 합치기
 - 단, 사이클 발생 시, 해당 간선은 포함 안함

 - 필요한 자료
  - union, find 함수
  - 부모 노드 테이블 parent
  - 간선 정보 edges > (cost, a, b)
    cost 가 기준이라 0번 값
'''

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


n, e = map(int, input().split())
parent = [i for i in range(n+1)]

edges = []
result = 0  # 신장 트리 비용 저장

# 모든 간선 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append(cost, a, b)

edges.sort()

# 간선 탐색
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost

print(result)