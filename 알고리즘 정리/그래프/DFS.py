'''
 - 시간복잡도 : O(N)
 - 재귀로 구현
 - 일반적으로 BFS 보다 느림
 - 이동한 정점의 값을 가지고 계산하는 경우 주로 사용

 - 연결 리스트(2차원), 기준 노드, 방문여부(1차원) 을 입력으로 받음
 >> 연결된 노드를 끝까지 갔다가 돌아오는 방식
'''

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    # 인접 노드 탐색
    for i in graph[v]:
        # 인접 노드에 방문한 적이 없다면 방문
        if not visited[i]:
            dfs(graph, i, visited)


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