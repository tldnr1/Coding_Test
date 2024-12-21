from collections import deque
'''
DFS(Depth First Search) 재귀 구현
 - O(N)
 - 일반적으로 BFS 보다 느림  >> stack 라이브러리를 활용하여 시간복잡도를 줄이는 테크닉도 존재
 - 이동한 정점의 값을 가지고 계속 계산하는 경우
'''
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드르 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

'''
BFS(Breadth First Search) 반복 구현
 - O(N)
 - 일반적으로 DFS 보다 빠름
 - 최단거리 문제
'''

# from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복  >> 처음에는 start가 queue에 들어있음
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    print()

'''
DFS 비재귀(반복) 구현
 - O(N)
 - bfs 처럼 구현함 >> deque 사용 (list도 가능하지만, deque이 성능이 더 좋으니까!)
 - 재귀에 비해 덜 간단함
 - 파이썬에서는 extend를 통해 BFS와 거의 동일하게 구현함!
    - extend() : deque의 메서드, 리스트 전체를 삽입함  // extendleft()는 왼쪽에 리스트 전체 삽입
'''
def dfs_iter(graph, start, visited):
    # 방문해야 할 노드를 stack 으로 표현
    stack = deque([start])
    # 스택이 빌 때까지 == 모든 노드를 방문할 때까지
    while stack:
        # 시작 노드 지정
        cur = stack.pop()
        # 현재 노드르 방문한 적이 있다면, continue
        if visited[cur]: continue
        # 그렇지 않다면, 1) 방문 표시 및 출력 / 2) 인접 노드를 스택에 추가 (extend)
        visited[cur] = True
        print(cur, end=' ')
        stack.extend(graph[cur][::-1])
        '''
        Q) 왜 [::-1] 로 넣나?
        A) stack.extend(list) 는 list를 stack 뒤에 붙여주는 과정
           그래서 다음에 탐색해야할 노드가 가장 뒤로 붙을 수 있도록 list를 뒤집어서 넣는 것
                e.g. cur == 1 인 경우
                     graph[cur] >> [2, 3, 8]
                     즉, 다음에 탐색해야할 노드는 2
                     [::-1] 을 안하고 extend 해버리면, 다음 pop 되는 값이 8이 된다!
                     그래서 역순으로 8, 3, 2 순으로 넣어줘서 2가 먼저 탐색되도록 해준 것
        '''
    print()


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

visited = [False] * node_count
bfs(graph, start_node, visited)

visited = [False] * node_count
dfs_iter(graph, start_node, visited)
