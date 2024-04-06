import sys
from collections import Counter

n = int(input())
components = Counter(sys.stdin.readline().split())

m = int(input())
to_find = sys.stdin.readline().split()

for find in to_find:
    try:
        if components[find] >= 1:
            components[find] -= 1
            print('yes', end=' ')
        else:
            print('no', end=' ')
    except:
        print('no')


'''
책의 답안
1. 이진 탐색
2. 계수 정렬
3. set 활용

이 중에서 set 활용을 잘 활용하면 좋을 것 같다
"부품 찾기" 문제에서 덜 확인한 부분이 부품의 개수가 무한한 점이다 (언급은 없었으나, 부품 유무만 확인한다는 점에서 같은 의미)
    따라서, 단순히 set으로 부품 유무만 빠르게 확인하고 넘어가는 것이 더 효율적인 것 같다
    
n = int(input())
array = set(map(int, input().split()))

n = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
'''