import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

cctv = []  # (cctv 번호, x, y)
for i in range(N):
    for j in range(M):
        if room[i][j] in [1, 2, 3, 4, 5]:
            cctv.append((room[i][j], i, j))

# cctv 종류
cctv_case = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]],
    [[0, 1, 2, 3]]
]

# 감시 방향 (북 동 남 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def watching(board, direction, x, y):  # cctv_case value 인자
    for d in direction:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            # 방 밖 or 벽 일 경우 종료
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = -1


def dfs(depth, room):
    global min_missing
    # cctv 전부 탐색 한 경우
    if depth == len(cctv):
        count = 0
        for i in range(N):
            count += room[i].count(0)
        min_missing = min(min_missing, count)
        return

    tempRoom = copy.deepcopy(room)
    cctvNum, x, y = cctv[depth]
    for i in cctv_case[cctvNum]:
        watching(tempRoom, i, x, y)
        dfs(depth+1, tempRoom)
        tempRoom = copy.deepcopy(room)  # 방 초기화


min_missing = int(1e9)
dfs(0, room)
print(min_missing)
