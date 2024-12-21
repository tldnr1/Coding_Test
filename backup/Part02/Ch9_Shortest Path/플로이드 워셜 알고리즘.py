# 우선 a -> b를 모두 저장한다(없으면 무한) - 2차원 리스트
# a -> Node -> b 의 경로의 비용을 확인해서, 더 짧다면 이 거리로 갱신한다
INF = int(1e9)

# 노드의 개수(n) 및 간선의 개수(e) 입력
n, e = map(int, input().split())
# 2차원 리스트를 INF로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]
# 자기자신은 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 각 간선에 대한 정보 입력받아 초기화
for _ in range(e):
    # a to b의 비용 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식 min(D_ab, D_ak + D+kb)
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('X')
        else:
            print(graph[a][b], end=' ')

    print()
