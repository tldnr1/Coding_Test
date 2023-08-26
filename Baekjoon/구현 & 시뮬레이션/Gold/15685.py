SIZE = 101
board = [[0] * SIZE for _ in range(SIZE)]

N = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def curve(d, g):
    dragons = [(0, 0), (dx[d], dy[d])]
    # 원점 기준 (a, b) 90도 => (-b, a)
    for _ in range(g):
        point = dragons[-1]  # 기준점
        for a, b in dragons[-2::-1]:
            na, nb = a - point[0], b - point[1]  # 기준점 원점으로
            na, nb = -nb + point[0], na + point[1]  # 회전 후 다시 기준점 x로
            dragons.append((na, nb))
    return dragons


for _ in range(N):
    x, y, direct, g = map(int, input().split())
    dragon = curve(direct, g)  # 원점 기준 계산
    for d in dragon:
        if 0 <= x+d[0] < SIZE and 0 <= y+d[1] < SIZE:
            board[y+d[1]][x+d[0]] = 1  # 예제 힌트에 나온 x, y가 생각한 거랑 반대

answer = 0
for i in range(SIZE-1):
    for j in range(SIZE-1):
        if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] == 1:
            answer += 1
print(answer)


'''
[드래곤 커브를 좌료가 아닌 '간선 방향' 으로 정리한 코드]
https://tmdrl5779.tistory.com/146

n = int(input())

graph = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(n):

    y, x, d, g = map(int, input().split(' '))
    graph[x][y] = 1

    # 커브 리스트 만들기
    curve = [d]
    for j in range(g):
        for k in range(len(curve) - 1, -1, -1):
            curve.append((curve[k] + 1) % 4)

    # 드래곤 커브 만들기
    for j in range(len(curve)):
        x += dx[curve[j]]
        y += dy[curve[j]]
        if x < 0 or x >= 101 or y < 0 or y >= 101:
            continue

        graph[x][y] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            answer += 1

print(answer)'''