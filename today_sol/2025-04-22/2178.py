import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().rstrip())) for _ in range(n)]

from collections import deque
def bfs(x, y):
    Q = deque()
    Q.append((x, y))

    while Q:
        x, y = Q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 1:
                    a[nx][ny] = a[x][y] + 1
                    Q.append((nx, ny))
    
    return a[n-1][m-1]

print(bfs(0, 0))
