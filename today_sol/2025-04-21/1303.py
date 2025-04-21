import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n: 열, m: 행
_map = [list(input().rstrip()) for _ in range(m)]  # 지도 입력받기

visited = [[False] * n for _ in range(m)]  # 방문 체크
dx = [0, 0, -1, 1]  # 상하좌우 이동
dy = [-1, 1, 0, 0]

from collections import deque
def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    current = _map[x][y]
    visited[x][y] = True

    cnt = 0
    while Q:
        x, y = Q.popleft()
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and _map[nx][ny] == current:
                visited[nx][ny] = True
                Q.append((nx, ny))

    return cnt

w_cnt = 0
b_cnt = 0
for i in range(m):
    for j in range(n):
        if _map[i][j] == 'W' and not visited[i][j]:
            w_cnt += bfs(i, j) ** 2
        elif _map[i][j] == 'B' and not visited[i][j]:
            b_cnt += bfs(i, j) ** 2

print(w_cnt, b_cnt)
