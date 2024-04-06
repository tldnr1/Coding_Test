n = int(input())
schedule = []  # 0번 초기화
for _ in range(n):
    t, p = map(int, input().split())
    schedule.append((t, p))

dp = [0] * (n+1)
# i일 까지 일했을 경우
for i in range(n):
    # i일이 일한 다음 일이 가능한 날부터 끝까지
    for j in range(i+schedule[i][0], n+1):
        # i일을 일하는 게 더 좋은 경우 갱신
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]
    #print(dp)

print(dp[-1])
