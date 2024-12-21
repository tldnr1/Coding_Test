n, m = map(int, input().split())

# 0원은 0개
d = [0] + [10001] * (m+1)

# 화폐 입력
coin = [int(input()) for _ in range(n)]
for c in coin:
    for i in range(m+1):
        # d[i-c]가 존재하는 경우
        if i >= c:
            d[i] = min(d[i-c] + 1, d[i])

if d[m] <= 10000:
    print(d[m])
else:
    print(-1)
