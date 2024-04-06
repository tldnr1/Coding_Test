for _ in range(3):
    x = input().split()
    cnt = x.count('0')

    if cnt == 1:
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('C')
    elif cnt == 4:
        print('D')
    elif cnt == 0:
        print('E')
