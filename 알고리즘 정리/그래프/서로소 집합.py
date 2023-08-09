'''
 - 시간복잡도 : O(V + M(1+log_2+M/V V))

 - find와 union을 통해 집합 만들기
  - find  : 해당 노드의 부모 노드 찾기
  - union : 두 노드의 부모 노드 합치기 (보통 작은 걸로)
  
 - 보통 union-find를 통해 cycle 판별을 주로 함
  - 각 간선 a to b에 대해
    모든 간선을 돌면서 a, b의 부모 노드 확인
    a b의 부모 노드가 같은 경우 == cycle

 - 필요한 자료
  - 부모 노드 저장할 parent 리스트 (1차원 리스트)
'''

''' cycle 판별 함수 '''
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아닌 경우 재귀로 끝까지 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드 간선 개수
v, e = map(int, input().split())
parent = [0] * (v+1)

# 자기 자신 부모로 초기화
for i in range(1, v+1):
    parent[i] = i

cycle = False

for a, b in range(e):
    # 사이클 발생 여부
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union(parent, a, b)

if cycle:
    print('cycle')
else:
    print('not cycle')
