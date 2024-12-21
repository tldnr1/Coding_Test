import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 최댓값 (global)
maxValue = 0

# 상, 하, 좌, 우
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# ㅗ, ㅜ, ㅏ, ㅓ 제외
def dfs(i, j, valueSum, cnt):
    global maxValue
    # 모양이 완성된 경우
    if cnt == 4:
        maxValue = max(maxValue, valueSum)
        return

    # 상, 하, 좌, 우 탐색
    for n in range(4):
        ni = i+move[n][0]
        nj = j+move[n][1]
        if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
            visited[ni][nj] = True
            # 방문 표시 및 제거(다른 모양도 지나가니까)
            dfs(ni, nj, valueSum + board[ni][nj], cnt+1)
            visited[ni][nj] = False


# ㅗ, ㅜ, ㅏ, ㅓ 모양
def etc(i, j):
    global maxValue
    for n in range(4):
        tmp = board[i][j]
        # move 중 3개만 사용하기 위한 인덱싱
        for k in range(3):
            # 012, 123, 230, 301
            t = (n+k)%4
            ni = i+move[t][0]
            nj = j+move[t][1]

            if not (0<=ni<N and 0<=nj<M):
                tmp = 0
                break
            tmp += board[ni][nj]
        # 최댓값 계산
        maxValue = max(maxValue, tmp)


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False
        etc(i, j)

print(maxValue)
