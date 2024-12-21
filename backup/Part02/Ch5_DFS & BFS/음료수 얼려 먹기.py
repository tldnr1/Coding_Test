from collections import deque

n, m = map(int, input().split())
tray = [list(map(int, input())) for _ in range(n)]

print(tray)
ice = deque()
ice_count = 0

for i in range(n):
    for j in range(m):
        if tray[i][j] == 0:
            ice.append((i, j))
            tray[i][j] = 1

            di = [-1, 1, 0, 0]
            dj = [0, 0, -1, 1]
            # 탐색 시작
            while ice:
                cur = ice.popleft()
                for x in range(4):
                    ni = cur[0] + di[x]
                    nj = cur[1] + dj[x]
                    # tray 밖이면 무시
                    if ni < 0 or ni >= n or nj < 0 or nj >= m:
                        continue
                    if tray[ni][nj] == 0:
                        ice.append((ni, nj))
                        tray[ni][nj] = 1
            # 한 덩어리 탐색 완료
            ice_count += 1

print(ice_count)

'''
# 책의 해설
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
            
print(result)
'''