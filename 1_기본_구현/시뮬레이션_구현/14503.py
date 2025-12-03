import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(d):
    return (d - 1 + 4) % 4

def solve():
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())

    # 0: 청소 안함, 1: 벽, 2: 청소 함
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    clean_count = 0

    # 청소 루프
    while True:
        # 현재 칸 청소
        if board[r][c] == 0:
            board[r][c] = 2
            clean_count += 1

        # 4방향 확인
        temp_d = d
        move_success = False

        for _ in range(4):
            # 반시계 90도 회전
            d = turn_left(d)

            # 한칸 전진
            nx = r + dx[d]
            ny = c + dy[d]

            # 앞이 벽이 아니고 청소 안된 빈칸인 경우 전진
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                r, c = nx, ny
                move_success = True
                break

        # 전진 성공 시 continue
        if move_success:
            continue

        # 전진 실패 시 후진
        back_d = (d + 2) % 4
        back_r = r + dx[back_d]
        back_c = c + dy[back_d]

        # 후진 칸이 벽이 아니면 continue
        if 0 <= back_r < n and 0 <= back_c < m and board[back_r][back_c] != 1:
            r, c = back_r, back_c
            continue
        # 후진 칸이 벽이면 break
        else:
            break

    print(clean_count)

solve()