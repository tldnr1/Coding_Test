from collections import deque
import sys
input = sys.stdin.readline

def turn_left(d):
    return (d + 3) % 4

def turn_right(d):
    return (d + 1) % 4

def solve():
    N = int(input())
    K = int(input())

    board = [[0] * (N + 1) for _ in range(N + 1)]   # 0: 빈 칸, 1: 뱀, 2: 사과
    for _ in range(K):
        r, c = map(int, input().split())
        board[r][c] = 2
    
    L = int(input())
    commands = {}
    for _ in range(L):
        X, C = input().split()
        commands[int(X)] = C

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0  # 초기 방향 오른쪽

    snake = deque([(1, 1)])
    x, y = 1, 1  # 머리 위치
    board[x][y] = 1

    time = 0
    while True:
        time += 1

        nx = x + dx[direction]
        ny = y + dy[direction]

        # 벽
        if not (1 <= nx <= N and 1 <= ny <= N):
            break

        # 뱀의 몸통
        if board[nx][ny] == 1:
            break

        # 이동한 곳에 사과 없으면 꼬리 제거거
        if board[nx][ny] == 0:
            tx, ty = snake.pop()
            board[tx][ty] = 0

        # 머리 이동
        snake.appendleft((nx, ny))
        board[nx][ny] = 1

        x, y = nx, ny


        if time in commands:
            dir_cmd = commands[time]
            if dir_cmd == 'L':
                direction = turn_left(direction)
            elif dir_cmd == 'D':
                direction = turn_right(direction)
    
    print(time)

solve()