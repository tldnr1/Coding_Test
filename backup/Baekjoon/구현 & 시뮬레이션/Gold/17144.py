import sys
import copy
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
# 공기청정기 위치
airCleaner = []
for i in range(R):
    if room[i][0] == -1:
        airCleaner.append(i)

dx = [-1, 0 ,1 ,0]
dy = [0, 1, 0, -1]
robot_top = airCleaner[0]
robot_bottom = robot_top + 1
def rotation():
    def top_rotate():  # 위쪽 회전
        d = 1  # 오른쪽 방향으로 시작
        before = 0
        x, y = robot_top, 1  # 공기청정기 머리부분의 바로 오른쪽 칸부터 시작
        while True:
            ax = x + dx[d]
            ay = y + dy[d]
            if ax == R or ay == C or ax == -1 or ay == -1:  # 현재 좌표가 꼭짓점인 경우
                d = (d - 1) % 4
                continue
            if x == robot_top and y == 0:  # 한 바퀴 회전 완료해서 공기청정기 좌표로 다시 돌아온 경우
                break
            room[x][y], before = before, room[x][y]
            x, y = ax, ay

    def bottom_rotate():  # 아래 회전
        d = 1  # 오른쪽 방향으로 시작
        before = 0
        x, y = robot_bottom, 1  # 공기청정기 아래부분의 바로 오른쪽 칸부터 시작
        while True:
            ax = x + dx[d]
            ay = y + dy[d]
            if ax == R or ay == C or ax == -1 or ay == -1:  # 현재 좌표가 꼭짓점인 경우
                d = (d + 1) % 4
                continue
            if x == robot_bottom and y == 0:  # 한 바퀴 회전 완료해서 공기청정기 좌표로 다시 돌아온 경우
                break
            room[x][y], before = before, room[x][y]
            x, y = ax, ay

    top_rotate()
    bottom_rotate()
"""def wind():
    a, b = airCleaner
    # 위쪽 a 부분 (좌-상-우-하 순서)
    for i in range(a-1):
        room[i+1][0] = room[i][0]
    for i in range(C-1):
        room[0][i] = room[0][i+1]
    for i in range(a):
        room[i][C-1] = room[i+1][C-1]
    for i in range(C-2, 0, -1):
        room[a][i+1] = room[a][i]
    room[a][1] = 0
    # 아래쪽 b 부분 (좌-하-우-상 순서)
    for i in range(b+1, R-1):
        room[i][0] = room[i+1][0]
    for i in range(C-1):
        room[R-1][i] = room[R-1][i+1]
    for i in range(R-2, b-1, -1):
        room[i+1][C-1] = room[i][C-1]
    for i in range(C-2, 0, -1):
        room[b][i+1] = room[b][i]
    room[b][1] = 0"""


def dust():
    temp = copy.deepcopy(room)
    for r in range(R):
        for c in range(C):
            if temp[r][c] >= 0:  # 확산 지점
                move_dust = temp[r][c] // 5
                move_cnt = 0

                dr = [-1, 0, 1, 0]
                dc = [0, -1, 0, 1]
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if nr < 0 or nc < 0 or nr >= R or nc >= C:
                        continue
                    if room[nr][nc] == -1:  # 공기청정기면 무시
                        continue
                    room[nr][nc] += move_dust
                    move_cnt += 1
             # 확산된 양 제거
                room[r][c] -= move_dust * move_cnt


for _ in range(T):
    dust()
    rotation()

# 남은 미세먼지 양 (공기청정기 -2 포함)
left_dust = 2
for i in range(R):
    left_dust += sum(room[i])
print(left_dust)
