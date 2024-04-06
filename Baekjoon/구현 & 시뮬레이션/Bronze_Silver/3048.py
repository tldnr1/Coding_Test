n1, n2 = map(int, input().split())
l1 = list(input().rstrip())
l1.reverse()
l2 = list(input().rstrip())
l = l1 + l2

t = int(input())
for _ in range(t):
    for i in range(n1+n2-1):
        # 인접한 두 개미가 다른 그룹이면 스왑
        if l[i] in l1 and l[i+1] in l2:
            l[i], l[i+1] = l[i+1], l[i]
            # 위치가 바뀐 개미가 선두면 종료
            if l[i+1] == l1[-1]:
                break
print("".join(l))
