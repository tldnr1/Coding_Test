import sys

input = sys.stdin.readline

# main
N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

cnt = 0
for s in size:
    if s%T == 0:
        cnt += s//T
    else:
        cnt += s//T + 1

print(cnt)
print((sum(size)) // P, sum(size) % P)