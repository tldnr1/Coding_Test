pos = input()
posY, posX = int(pos[1]), ord(pos[0]) - 96

# (y, x)
moves = [(2, -1), (2, 1), (-2, -1), (-2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]

cnt = 0
for move in moves:
    ny = posY + move[0]
    nx = posX + move[1]
    # 체스판 밖이면 무시
    if ny < 1 or ny > 8 or nx < 1 or nx > 8:
        continue
    cnt += 1

print(cnt)
