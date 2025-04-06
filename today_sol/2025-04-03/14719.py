import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))
answer = 0

for i in range(1, w-1):
    left = max(block[ :i])
    right = max(block[i+1: ])
    _min = min(left, right)
    if _min > block[i]:
        answer += _min - block[i]
 
print(answer)