# Q35 - 못생긴 수
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
dp[0] = 1

c2, c3, c5 = 0, 0, 0
n2, n3, n5 = 2, 3, 5

for i in range(1, n):
    dp[i] = min(n2, n3, n5)
    # c를 참고해서 다음 숫자 선택
    if dp[i] == n2:
        c2 += 1
        n2 = dp[c2] * 2
    if dp[i] == n3:
        c3 += 1
        n3 = dp[c3] * 3
    if dp[i] == n5:
        c5 += 1
        n5 = dp[c5] * 5

print(dp[n-1])