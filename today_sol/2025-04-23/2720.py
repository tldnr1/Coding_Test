t = int(input())
money = [25, 10, 5, 1]

for _ in range(t):
    c = int(input())
    cnt = [0, 0, 0, 0]

    for i, m in enumerate(money):
        if c >= m:
            cnt[i] = c // m
            c %= m
    print(*cnt)
