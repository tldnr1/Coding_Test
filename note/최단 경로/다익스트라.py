'''
 - 시간복잡도 : O(ElogV)
 - 특정 노드에서 다른 모든 노드로의 최단 경로

 - 우선순위 큐 사용 : heapq 에 (비용, 간선) 저장
 - 비용이 가장 적게 드는 경로를 선정
    이후, 이 노드를 거치는 것이 비용이 적게 드는 노드가 있다면
    해당 노드의 최단 경로를 갱신

 - 필요로 하는 자료들
    - 노드 간선 정보 (연결 리스트)
    - 최단 거리 테이블 (1차원 리스트)
    - 비용 기준 우선순위 큐 (heapq)
'''
import heapq
INF = int(1e9)

# 노드, 간선 개수
n, e = 5, 7
# 노드 연결 정보
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블
distance = [INF] * (n + 1)

# 시작 노드
start = int(input())
# 간선 정보 입력
for _ in range(e):
    # a to b 의 비용 c
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

def dijkstra(start):
    q = []
    # 시작 지점 비용 0으로 추가, 비용 갱신
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최소 비용 간선 꺼냄
        # 참고로 dist는 graph의 cost가 아니다
        #    dist는 now_node 까지의 최소 비용 값이다!
        dist, now_node = heapq.heappop(q)
        # 방문한 적 있는 노드 무시 == now_node를 거치는 경우가 더 긴 경우
        if distance[now_node] < dist:
            continue
        # 인접 노드들 중에서 now_node를 거치는 게 더 비용이 적은게 있는지 확인
        for i in graph[now_node]:  # i == (b, cost)
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, [i[0]]))
