from collections import deque
import copy

n = int(input())

indegree = [0] * (n+1)
time = [0] * (n+1)
# 간선 정보
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:  # 시간, -1 제외
        indegree[i] += 1
        graph[x].append(i)

# def topology_sort()
result = copy.deepcopy(time)
q = deque()
# 진입차수 0 담기
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    #print(now, result, indegree)
    # 연결된 노드 확인
    for i in graph[now]:
        # 시간 갱신
        # max인 이유는 선수 과목이 여러 개인 경우를 위함
        #print(now, i, result[i], result[now], time[i])
        result[i] = max(result[i], result[now] + time[i])
        indegree[i] -= 1
        # 새로 진입차수가 0이 된 노드 추가
        if indegree[i] == 0:
            q.append(i)

for i in range(1, n+1):
    print(result[i])
