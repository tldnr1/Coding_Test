# 최단 거리가 짧은 노드 확인 > 인접 노드들을 확인
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 각 노드에 연결되어 있는 노드 정보 입력
graph = [[] for i in range(n+1)]
# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선(Edge) 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a to b의 비용이 c
    graph[a].append((b, c))

for g in graph:
    print(g)

# start : 시작 노드
def dijkstra(start):
    # (거리, 노드) 저장할 heapq
    q = []
    # 시작 노드 거리 0, 힙큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단 거리가 가장 짧은 노드 꺼내기 (heapq라 가장 앞이 최단 거리)
        dist, now = heapq.heappop(q)
        # 처리된 적 있는 노드 무시 == 더 짧은 거리가 존재
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 인접 노드 거리 확인
        for i in graph[now]:
            cost = dist + i[1]  # i = (b, c)
            # 현재 노드를 거쳐가는 거리가 더 짧으면 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력 (from start)
for i in range(1, n+1):
    # 도달 못하는 경우 X 출력
    if distance[i] == INF:
        print("X")
    else:
        print(distance[i])
