import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
# a to b의 비용(시간) t : edge_graph[a] = (b, t)
edge_graph = [[] for _ in range(n+1)]
# 간선 정보 입력
for _ in range(m):
    # x to y의 비용 z
    x, y, z = map(int, input().split())
    edge_graph[x].append((y, z))

# 최소 시간 측정 : 1번의 최소시간 = time[1]
time = [INF] * (n+1)

def dijstra(start):
    # 최소 시간 우선순위 큐(힙큐) : (min_time, direction)
    q = []
    # 시작점 초기화
    time[start] = 0
    heapq.heappush(q, (0, start))
    # start에서 모든 노드까지 최소 거리 계산
    while q:
        dist, node_now = heapq.heappop(q)
        # 방문한 노드 무시 = node_now 거치는 게 더 오래 걸림
        if time[node_now] < dist:
            continue
        # node_now 거치는 게 좋으면 인접 노드 갱신 필요한지 확인
        # == start~A의 기존 최소값 보다, start~node_now~A 가 더 작은지 확인
        for node_around in edge_graph[node_now]:
            # dist = start~node / node_around[1] = node_now~A
            cost = dist + node_around[1]
            # time[node_around[0]] = start~A
            if cost < time[node_around[0]]:
                time[node_around[0]] = cost
                heapq.heappush(q, (cost, node_around[0]))

dijstra(start)

city_cnt = 0
max_time = 0
# 0번 인덱스 제외
for t in time[1:]:
    # 도달 가능한 도시인 경우
    if t != INF:
        city_cnt += 1
        max_time = max(max_time, t)

# 시작 노드 제외
print(city_cnt - 1, max_time)
