# k의 배수 중 n에 가장 가까운 수를 찾기  >> (n//k) * k
# 이후 남은 횟수 더해주기

n, k = map(int, input().split())
cnt = 0

while True:
    target = (n//k) * k
    cnt += n - target  # 배수를 만들기 위해 1을 뺀 횟수
    n = target

    # n < k 가 되어서 배수를 더 만들 수 없을 때 반복문 탈출
    if n < k:
        break

    # k로 나누기
    cnt += 1
    n //= k

# 반복문 탈출 후, 남은 1 빼기 횟수
cnt += n - 1
print(cnt)

'''
# 단순하게 생각한 코드
# n이 매우 커지면 시간이 너무 오래 걸림

n, k = map(int, input().split())

cnt = 0
while n != 1:
    if n % k == 0:
        n = n // k
        cnt += 1
        #print(n)
    else:
        n = n - 1
        cnt += 1
        #print(n)

print(cnt)
'''