'''
 - 시간복잡도 : O(log N)

 - bottom, top의 중간점인 mid를 옮겨가며 탐색
 - ** 이진탐색을 위한 리스트는 정렬되어 있어야 함
 - 최선의 정답을 찾기 위한 경우라면, 일단 정답을 저장한 뒤에
    조건을 좀 더 높여보며 탐색을 이어나가면 됨
'''

l = [1, 5, 6, 7, 2, 3, 8, 4, 9]
target = 7

# 이진 탐색
l.sort()  # 이진 탐색을 위해서는 정렬된 리스트가 필요
bottom = l[0]
top = l[-1]

while bottom <= top:
    mid = (bottom + top) // 2

    if target > mid:
        bottom = mid + 1
    elif target < mid:
        top = mid - 1
    else:
        print(mid)
        break
