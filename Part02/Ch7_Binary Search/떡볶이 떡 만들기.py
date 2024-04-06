import sys

n, m = map(int, input().split())
rice_cake = list(map(int, sys.stdin.readline().split()))

h_result = 0
top = max(rice_cake)
bottom = 0
while bottom <= top:
    mid = (bottom + top) // 2
    cutting = sum(rice - mid for rice in rice_cake if rice > mid)
    print(cutting, bottom, top, mid)
    # 필요 이상이면, 최선의 정답을 기록 후 일단 높이를 올려봄
    if cutting >= m:
        h_result = mid
        bottom = mid + 1
    else:
        top = mid - 1

print(h_result)
