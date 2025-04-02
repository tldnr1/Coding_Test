t = int(input())

for _ in range(t):
    n = int(input())
    binary = bin(n)[2:]
    
    for i, num in enumerate(str(binary)[::-1]):
        if num == '1':
            print(i, end=' ')