import sys
input = sys.stdin.readline

l = input().rstrip()
s = []
answer = 0
tmp = 1

for i in range(len(l)):
    if l[i] == '(':
        s.append(l[i])
        tmp *= 2
    elif l[i] == '[':
        s.append(l[i])
        tmp *= 3
    elif l[i] == ')':
        if not s or s[-1] == '[':
            answer = 0
            break
        if l[i-1] == '(':
            answer += tmp
        s.pop()
        tmp //= 2
    elif l[i] == ']':
        if not s or s[-1] == '(':
            answer = 0
            break
        if l[i-1] == '[':
            answer += tmp
        s.pop()
        tmp //= 3


if s: # 스택이 비어있지 않다면
    print(0)
else:
    print(answer)