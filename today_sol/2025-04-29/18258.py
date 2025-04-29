import sys
from collections import deque

n = int(input())
Q = deque([])

for i in range(n):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        Q.append(com[1])
    elif com[0] == 'pop':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.popleft())
    elif com[0] == 'size':
        print(len(Q))
    elif com[0] == 'empty':
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])
    elif com[0] == 'back':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[-1])