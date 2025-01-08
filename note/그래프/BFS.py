'''
 - 시간복잡도 : O(N)
 - 반복 구현
 - 일반적으로 DFS 보다 빠름
 - 최단거리 탐색에 주로 사용

 - queue 자료구조 사용
 - 연결 리스트(2차원), 시작점, 방문여부(1차원) 을 입력으로 받음
 >> 연결된 노드를 가까운 순서부터 전부 방문하는 방식
'''
from collections import deque

def bfs(graph, start, visited):
    # 시작점 추가 및 방문처리
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        # 주변 노드 탐색 후 방문처리
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# p.134 의 예제에 나온 그래프
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 전체 노드 개수
node_count = 9
# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)

# 시작 노드부터 탐색
start_node = 1
visited = [False] * node_count
dfs(graph, start_node, visited)
print()