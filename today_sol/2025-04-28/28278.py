import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

Q = deque([])
for _ in range(n):
    c = list(input().split())
    if c[0] == '1':
        Q.append(c[1])
    elif c[0] == '2':
        if not Q:
            print(-1)
        else:
            i = Q.pop()
            print(i)
    elif c[0] == '3':
        print(len(Q))
    elif c[0] == '4':
        if not Q:
            print(1)
        else:
            print(0)
    elif c[0] == '5':
        if not Q:
            print(-1)
        else:
            print(Q[-1])