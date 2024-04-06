# 24 * 60 * 60 = 86,400 >> O(N) 으로 구현해도 시간 내에 작동 가능
n = int(input())

cnt = 0
for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour)+str(minute)+str(second):
                cnt += 1
print(cnt)
