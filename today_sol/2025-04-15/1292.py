a, b = map(int, input().split())

numbers = []
for i in range(1, b + 1):
    for _ in range(i):
        numbers.append(i)

print(sum(numbers[a-1: b]))
