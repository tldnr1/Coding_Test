n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1


from collections import deque
def bfs(x, y):
    if board[x][y] == 0:
        return 0
    
    Q = deque()
    Q.append((x, y))
    board[x][y] = 0 # visited

    cnt = 0
    while Q:
        x, y = Q.popleft()
        cnt += 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                board[nx][ny] = 0 # visited
                Q.append((nx, ny))

    return cnt
    
answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            cnt = bfs(i, j)
            answer = max(answer, cnt)
print(answer)
    