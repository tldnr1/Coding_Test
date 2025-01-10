# Q33 - 퇴사
import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []
dp = [0] * (n+1)

# 일정표 입력
for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# dp 시작
'''
n번째 날의 일정을 포함 + 그 이후의 최대값 vs 포함안함 을 비교
그래서 마지막 날부터 거꾸로 내려오면서 dp 계산
dp[i] = max(p[i] + dp[t[i]+i], max_value) -> max_value는 현재까지의 최대 이익
'''
max_value = 0
for i in range(n-1, -1, -1):
    time = t[i] + i
    # 기간 안에 끝나는 경우
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 기간을 초과하는 경우
    else:
        dp[i] = max_value

print(max_value)
