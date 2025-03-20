# Q36 - 편집 거리
# Hint - 2차원 배열 초기화를 통해 가능함

def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    # 각 문자열에 대한 0번째에 0 ... len 으로 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j

    # 최소 편집 거리 계산
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 문자가 같은 경우 좌상단 값 가지고 옴
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 다른 경우 min으로 삽입(좌), 삭제(상), 교체(좌상) 중 골라옴
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[n][m]


str1 = input()
str2 = input()

print(edit_dist(str1, str2))