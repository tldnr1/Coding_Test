import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    numbers = list(map(int, input().split()))
    for number in numbers:
        graph[i].append(number)

# 최하층+1 ~ 최상층 까지 아래층 에서 큰 것만 고르며 올라옴
for i in range(n-2, -1, -1):
    # 0,1 ~ i-2,i-1 까지
    for j in range(i+1):
        graph[i][j] += max(graph[i+1][j], graph[i+1][j+1])

print(graph[0][0])


'''
위에서 아래로 내려오는 풀이 : https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-1932-%EC%A0%95%EC%88%98-%EC%82%BC%EA%B0%81%ED%98%95-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python

n = int(input())
dp = []

for i in range(n):
    dp.append(list(map(int ,input().split())))

for i in range(1, n):
    for j in range(0, i+1):
        # 왼쪽 끝
        if j == 0:
            dp[i][0] += dp[i-1][0]
        # 오른쪽 끝
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        # 나머지 위에서 2가닥 내려오는 부분들
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
            
print(max(dp[n-1]))
'''