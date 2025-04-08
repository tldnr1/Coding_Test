import sys
input = sys.stdin.readline

n = int(input())
candy = [list(input().rstrip()) for _ in range(n)]
result = 0

def checkBombo():
    global result
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if candy[i][j] == candy[i][j+1]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1
    
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if candy[j][i] == candy[j+1][i]:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 1

for i in range(n):
    for j in range(n-1):
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        checkBombo()
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

        candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
        checkBombo()
        candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]

print(result)
