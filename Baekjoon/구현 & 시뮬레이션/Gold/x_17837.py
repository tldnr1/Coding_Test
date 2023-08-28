import sys
import copy
input = sys.stdin.readline

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
board.append([2] * N)  # 테두리 Blue(2) 로 고정
board.insert(0, [2] * N)
for i in range(N+2):
    board[i].insert(0,2)
    board[i].append(2)

# 말의 위치(knight 는 상태)를 저장할 3차원 배열 (2차원 + stack)
knight_pos = [[[] for _ in range(N+2)] for _ in range(N+2)]
knight = [list(map(int, input().split())) for _ in range(K)]
for i in range(K):
    x, y, d = knight[i]
    knight[i][2] -= 1  # move 0~3 을 위해 인덱스 조정
    knight_pos[x][y].append(i)

# 우, 좌, 상, 하
move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
# 시작 상태 비교
start_state = copy.deepcopy(knight)
# 턴 횟수
cnt = 0

# 탐색 시작
while cnt <= 10:
    cnt += 1
    for i in range(K):
        print('---------------------------------------')
        print('now: ', i)
        for k in knight:
            print(k)
        for pos in knight_pos:
            print(pos)

        x, y, d = knight[i]
        nx = x + move[d][0]
        ny = y + move[d][1]
        # 이동할 칸의 색깔(상태)
        next_state = board[nx][ny]
        if next_state == 0:
            print('used state:', 0)
            print(12345, i, (x, y), (nx, ny), knight_pos[x][y], d)
            # 옮긴 말의 현 idx
            idx = knight_pos[x][y].index(i)
            move_knight = knight_pos[x][y][idx:]
            for move_k in move_knight:
                knight[move_k] = nx, ny, knight[move_k][2]
                knight_pos[nx][ny].append(move_k)
                knight_pos[x][y].remove(move_k)
        elif next_state == 1:
            print('used state:', 1)
            print(12345, i, (x, y), (nx, ny), knight_pos[x][y], d)
            idx = knight_pos[x][y].index(i)
            move_knight = knight_pos[x][y][idx:]
            move_knight.reverse()
            for move_k in move_knight:
                knight[move_k] = nx, ny, knight[move_k][2]
                knight_pos[nx][ny].append(move_k)
                knight_pos[x][y].remove(move_k)
        else:  # next_state == 2
            print('used state:', 2, d)
            # 반대 방향 확인 (0~1 / 2~3)
            if d % 2 == 0:
                d += 1
            else:
                d -= 1
            nx = x+move[d][0]
            ny = y+move[d][1]
            #idx = knight_pos[x][y].index(i)
            print(12345, i, (x, y), (nx, ny), knight_pos[x][y], idx, d)
            # 뒤쪽도 파란색이면 방향만 변경
            if board[nx][ny] == 2:
                knight[i] = x, y, d
                continue
            # 변경 된 방향으로 혼자 이동
            knight_pos[nx][ny].append(i)
            knight_pos[x][y].remove(i)
            knight[i] = nx, ny, d

            """# 쌓인 말들에 대한 이동
            move_knight = knight_pos[x][y][idx:]
            print('move_knight: ', move_knight)
            for move_k in move_knight:
                knight[move_k] = nx, ny, knight[move_k][2]
                knight_pos[nx][ny].append(move_k)
                knight_pos[x][y].remove(move_k)
            # 기준 말 방향 변경
            knight[i] = nx, ny, d"""

        if len(knight_pos[nx][ny]) >= 4:
            print(cnt)
            exit()

    if knight == start_state:
        print(-1)
        exit()
# 해결이 안되는 경우
print(-1)