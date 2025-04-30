n = int(input())
t, p = [0], [0]

for _ in range(n):
    _t, _p = map(int, input().split())
    t.append(_t)
    p.append(_p)


dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])
    finihsh_day = i + t[i] - 1
    if finihsh_day <= n:
        dp[finihsh_day] = max(dp[finihsh_day], dp[i - 1] + p[i])

print(max(dp))