n = int(input())

arr = [int(input()) for _ in range(n)]
arr.sort()  # arr = sorted(arr, reverse=True) 로 먼저 내림차순 정렬도 가능

for num in arr[::-1]:
    print(num, end=' ')
