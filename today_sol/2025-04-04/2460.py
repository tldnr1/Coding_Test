_max = 0
now = 0

for _ in range(10):
    o, i = map(int, input().split())
    now += i - o

    if now >= _max:
        _max = now

print(_max)
