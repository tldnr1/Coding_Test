def is_prime(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    if n % 2 == 0:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return 0
        return 1


n = int(input())
numbers = list(map(int, input().split()))

cnt = 0
for num in numbers:
    cnt += is_prime(num)

print(cnt)
