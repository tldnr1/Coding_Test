n, l = map(int, input().split())
trap = [list(map(int, input().split())) for _ in range(n)]

t = 0
now = 0
# 기다린 시간 더하기
for d, r, g in trap:
    t += d - now
    now = d
    # 초록 불이 되려면 필요한 시간
    if t % (r + g) < r:
        t += r - t % (r + g)
# 남은 거리 이동
t += l - now
print(t)
