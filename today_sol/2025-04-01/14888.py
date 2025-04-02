n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

max_result = -1e9
min_result = 1e9

def dfs(depth, total, plus, minus, multi, divide):
    global max_result, min_result
    if depth == n:
        max_result = max(total, max_result)
        min_result = min(total, min_result)
        return
        
    # 재귀처리
    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multi, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multi, divide)
    if multi:
        dfs(depth + 1, total * num[depth], plus, minus, multi - 1, divide)
    if divide:
        dfs(depth+1, int(total / num[depth]), plus, minus, multi, divide-1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(max_result)
print(min_result)