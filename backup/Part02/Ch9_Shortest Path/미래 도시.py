INF = int(1e9)
n, m = map(int, input().split())
# 최단 거리를 담을 2차원 리스트, 0번 미사용
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신 제거
for i in range(1, n+1):
    graph[i][i] = 0

# 연결된 노드 입력받기, 거리 1 고정 & 양방향
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 모든 노드 탐색
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # k를 거치는게 더 빠른지 확인
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# x, k 입력
x, k = map(int, input().split())

# k를 거치고 x로 이동
distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)
