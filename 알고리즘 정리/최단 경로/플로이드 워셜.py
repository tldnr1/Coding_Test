'''
 - 시간복잡도 : O(N ^ 3)
 - 모든 노드에서 다른 모든 노드로의 최단 경로

 - a to b 를 우선 저장 (없으면 INF)
 - 이후 k에 대해 'a to k to b' 가 더 짧으면 갱신
    점화식 : D[a][b] = min(D[a][b], D[a][k] + D[k][b])

 - O(n^3)의 복잡도 이므로 n이 작을 때 사용 가능하다
 - 필요로 하는 자료들
    - 간선 연결 정보 (2차원 리스트)
'''
INF = int(1e9)
# 노드 간선 개수
n, e  = map(int, input().split())

# 2차원 리스트로 간선 연결 저장
graph = [[INF] * (n+1) for _ in range(n+1)]
# 자기자신은 0
for i in range(1, n+1):
    graph[i][i] = 0
# 간선 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost

# 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k], graph[k][b])

# 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('X')
        else:
            print(graph[a][b], end=' ')