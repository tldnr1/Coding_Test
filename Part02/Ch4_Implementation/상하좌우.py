n = int(input())
plans = input().split()

# 시작 위치
posY, posX = 1, 1
for plan in plans:
    if plan == 'L':
        if posX > 1:
            posX -= 1
    elif plan == 'R':
        if posX < n:
            posX += 1
    elif plan == 'U':
        if posY > 1:
            posY -= 1
    elif plan == 'D':
        if posY < n:
            posY += 1

print(posY, posX)


'''
# 책의 답안
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획 하나씩 확인
for plan in plans:
for i in range(len(move_types)):  >> dx, dy 에서 index로 탐색하기 위해 range로 반복문 실행
    if plan == move_types[i]:  
        nx = x + dx[i]  >> 이동 후 값을 임의로 저장해서 확인절차 가능하게 하기
        xy = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < i or ny < i or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
'''