# Q32 - 정수 삼각형
import sys
input = sys.stdin.readline

n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

# dp 시작
'''
1) 좌 상단에서 내려옴
2) 상단에서 내려옴
'''
for i in range(1, n): # 첫 줄 제외
    for j in range(i+1):
        if j == 0: # 좌상단 없음
            dp[i][j] += dp[i-1][j]
        elif j == i: # 상단 없음
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))
