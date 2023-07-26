n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

result = 0

# first k번 + second 1번
while True:
    for _ in range(k):
        if m == 0:
            break
        result += first
        m -= 1

    if m == 0:
        break
    result += second
    m -= 1

print(result)


'''
# 반복되는 수열을 계산해서 first, second가 몇 번 나오는지 수식으로 나타낸 경우
# first : int(m / (k+1)) * k  +  m % (k+1)
# second : m - first_cnt

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

# first 가 더해지는 횟수
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second

print(result)
'''