gear = [list(map(int, input())) for _ in range(4)]


def roll(i, direct):
    if direct == -1:
        temp = gear[i].pop(0)
        gear[i].append(temp)
    elif direct == 1:
        temp = gear[i].pop()
        gear[i].insert(0, temp)


K = int(input())
for _ in range(K):
    num, direct = map(int, input().split())

    # 왼쪽 회전
    temp = direct * -1
    roll_gear = []
    for i in range(num-1, 0, -1):  # i 기준 i-1 회전 판단
        if gear[i][6] != gear[i-1][2]:
            roll_gear.append((i-1, temp))
            temp *= -1
        else:
            break
    for r, d in roll_gear:
        roll(r, d)

    # 오른쪽 회전
    temp = direct * -1
    roll_gear = []
    for i in range(num, 4):  # i-1 기준 i 회전 판단
        if gear[i-1][2] != gear[i][6]:
            roll_gear.append((i, temp))
            temp *= -1
        else:
            break
    for r, d in roll_gear:
        roll(r, d)

    # 기준 톱니바퀴 회전
    roll(num-1, direct)

answer = 0
for i in range(4):
    if gear[i][0] == 1:
        answer += 2 ** i
print(answer)
