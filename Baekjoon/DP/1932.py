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
