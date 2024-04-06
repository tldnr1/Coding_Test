from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

# 우, 하, 좌, 상 순서
dx = [0, 1, 0, -1]  # n
dy = [1, 0, -1, 0]  # m


def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖은 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if maze[nx][ny] == 0:
                continue
            # 처음 방문하는 곳에 거리 기록
            if maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
    return maze[n-1][m-1]


# 출발 위치 1,1 == 좌표 0,0
print(bfs(0, 0))
