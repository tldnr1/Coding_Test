x = int(input())
# 연산 횟수 계산할 캐시
cache = [0] * (x + 1)
# 2부터 x까지 연산
for i in range(2, x+1):
    # x에서 1 빼기
    cache[i] = cache[i-1] + 1
    # 이후 나누어 떨어지는 관계
    if i%2 == 0:
        cache[i] = min(cache[i//2]+1, cache[i])
    if i%3 == 0:
        cache[i] = min(cache[i//3]+1, cache[i])
    if i%5 == 0:
        cache[i] = min(cache[i//5]+1, cache[i])
print(cache[x])
