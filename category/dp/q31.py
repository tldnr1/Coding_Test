# Q31 - 금광
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # dp 테이블 초기화
    dp = []
    for i in range(n):
        dp.append(data[i*m:(i+1)*m])

    # dp 진행
    '''
    현재 위치로 오는 값이
    1) 왼쪽 위에서 오는 경우
    2) 왼쪽에서 오는 경우
    3) 오른쪽 아래에서 오는 경우
    '''
    for j in range(1, m):
        for i in range(n):
            if i == 0:  # 왼쪽 위 제외
                dp[i][j] += max(dp[i][j-1], dp[i+1][j-1])
            elif i == n-1: # 오른쪽 아래 제외
                dp[i][j] += max(dp[i-1][j-1], dp[i][j-1])
            else: # 모두 가능
                dp[i][j] += max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

    # 마지막 m번째 열의 max 찾기
    res = 0
    for i in range(n):
        res = max(res, dp[i][m-1])

    print(res)

# # 교재 코드
# for tc in range(int(input())):
#     n, m = map(int, input().split())
#     array = list(map(int, input().split()))
#
#     dp = []
#     index = 0
#     for i in range(n):
#         dp.append(array[index:index+m])
#         index += m
#
#     for j in range(1, m):
#         for i in range(n):
#             if i == 0:
#                 left_up = 0
#             else:
#                 left_up = dp[i-1][j-1]
#             if i == n-1:
#                 left_down = 0
#             else:
#                 left_down = dp[i+1][j-1]
#
#             left = dp[i][j-1]
#             dp[i][j] = dp[i][j] + max(left_up, left_down, left)
#
#     result = 0
#     for i in range(n):
#         result = max(result, dp[i][m-1])
#
#     print(result)