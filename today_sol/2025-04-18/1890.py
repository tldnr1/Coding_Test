import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == j == n - 1:
            break

        x = board[i][j]
        # move right
        if j + x < n:
            dp[i][j + x] += dp[i][j]
        # move down
        if i + x < n:
            dp[i + x][j] += dp[i][j]

print(dp[n-1][n-1])
