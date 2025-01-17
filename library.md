# sort
```
# iterable 대상으로 사용
data = [('p1', 1), ('p2', 2), ('p3', 3)]
result = sorted(data, key = lambda x: x[1])  # 2번째 속성을 기준으로 정렬

data.sort() 도 가능
```

# itertools
```
data = ['A', 'B', 'C']

# 순열
from itertools import permutations
result = list(permutations(data, 3))

# 순열 (중복 포함)
from itertools import product
result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열(중복 허용)

# 조합
from itertools import combinations
result = list(combinations(data, 2))    # 2개를 뽑는 모든 조합

# 조합 (중복 포함)
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2))
```

# heapq
```
# heap 정렬 구현 위해 주로 사용

import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)    # Max heap의 경우 -value
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))     # Max heap의 경우 -heapq.heappop(h)
    return result
```

# bisect
```
# "정렬된 리스트"에서 값이 특정 범위에 속하는 원소의 개수 를 구할 때 유리
# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 기본적인 사용법
a = [1, 2, 4, 4, 8]
         c1    c2
x = 4

bisect_left(a, x)   # 2 반환 (c1)
bisect_right(a, x)  # 4 반환 (c2)
```

# deque
```
from collections import deque
Q = deque([])

Q.append(1)
Q.popleft()

# popleft() : 좌측에서 1개 제거
# pop()     : 우측에서 1개 제거
# appendleft(x) : 좌측에 x 추가
# apppend(x)    : 우측에 x 추가
```

# math
```
# 최대공약수
import math

print(math.gcd(21, 14))     # result : 7
```