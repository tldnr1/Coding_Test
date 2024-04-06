n, m = map(int, input().split())
a, b, direction = map(int, input().split())

# n * m 맵 생성
d = [list(map(int, input().split())) for _ in range(n)]

# 북, 동, 남, 서 (좌측 상단 0,0)
dy = [-1, 0, 1, 0]  # a
dx = [0, 1, 0, -1]  # b

# 처음 위치 방문 표시
d[a][b] = 1

# 지나온 경로 및 개수
move = [(a, b)]
move_cnt = 0
while move:
    for i in range(1, 5):
        current_pos = move[-1]
        next_move = (direction + i) % 4
        ny = current_pos[0] + dy[next_move]
        nx = current_pos[1] + dx[next_move]

        # 이동 가능한 경우
        if d[ny][nx] == 0:
            d[ny][nx] = 1
            move.append((ny, nx))

    # 4방향 모두 이동 불가능한 경우
    move.pop()
    move_cnt += 1

print(move_cnt)
