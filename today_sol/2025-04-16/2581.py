def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    # 홀수 중 확인
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


m = int(input())
n = int(input())
_min = int(1e9)
_sum = 0

for i in range(m, n + 1):
    if is_prime(i):
        if _min == int(1e9):
            _min = i
        _sum += i

if _sum == 0:
    print(-1)
else:
    print(_sum)
    print(_min)
