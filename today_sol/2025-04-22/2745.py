num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = input().split()
result = 0
for i, num in enumerate(n[::-1]):
    result += int(b) ** i * num_list.index(num)
print(result)
