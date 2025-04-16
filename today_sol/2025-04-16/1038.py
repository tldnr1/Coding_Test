from itertools import combinations

N = int(input())

numbers = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        num = ''.join(list(map(str, reversed(list(j)))))
        numbers.append(int(num))


numbers.sort()
if N >= len(numbers):
    print(-1)
else:
    print(numbers[N])
