'''
 - 시간복잡도 : O(V + E)

 - 진입차수가 작은 노드부터 탐색
 - 모든 원소를 방문하기 전에 큐가 비어버리면 사이클
    사이클에 포함된 원소 중 어떤 원소도 큐에 들어가지 못함

    따라서, 위상 정렬 문제는 사이클이 없다고 가정

 - 필요한 자료
  - 진입차수 리스트(1차원)
  - 간선 정보 (2차원 리스트)
  - 진입차수가 0이 된 노드를 담을 큐
'''

from collections import deque

v, e = map(int, input().split())

# 모든 노드에 대한 진입차수 초기화
indegree = [0] * (v + 1)
# 간선 정보 초기화
graph = [[] for _ in range(v+1)]

# 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # a -> b 이므로 b 진입차수 +1
    indegree[b] += 1

# 위상 정렬
def topology_sort():
    result = []
    q = deque()

    # 처음 시작은 진입차수 0인 노드 삽입
    # 없으면 사이클
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q: # 큐가 v회 돌지 못하면 사이클, 이 코드는 측정하지 않음
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드 확인
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 된 노드 추가
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()