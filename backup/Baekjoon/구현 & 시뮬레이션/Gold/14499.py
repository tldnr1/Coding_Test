N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))
for i in range(K):
    move[i] -= 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0] * 6
state_A = [4, 1, 3, 6]  # 가로
state_B = [2, 1, 5, 6]  # 세로


def roll(x):
    if x == 0:  # 동쪽
        temp = state_A.pop()
        state_A.insert(0, temp)
        state_B[1], state_B[3] = state_A[1], state_A[3]
    elif x == 1:  # 서쪽
        temp = state_A.pop(0)
        state_A.append(temp)
        state_B[1], state_B[3] = state_A[1], state_A[3]
    elif x == 2:  # 북쪽
        temp = state_B.pop(0)
        state_B.append(temp)
        state_A[1], state_A[3] = state_B[1], state_B[3]
    elif x == 3:  # 남쪽
        temp = state_B.pop()
        state_B.insert(0, temp)
        state_A[1], state_A[3] = state_B[1], state_B[3]
    return state_A[1]-1, state_A[3]-1  # 상단, 하단 값 반환


answer = []
for m in move:
    nx = x + dx[m]
    ny = y + dy[m]
    if 0 <= nx <= N-1 and 0 <= ny <= M-1:  # 범위 내부
        x, y = nx, ny
        top, bottom = roll(m)
        # 바닥 값 확인
        if board[x][y] == 0:
            board[x][y] = dice[bottom]
        else:
            dice[bottom] = board[x][y]
            board[x][y] = 0
        answer.append(dice[top])

for a in answer:
    print(a)
