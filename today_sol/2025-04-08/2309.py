smalls = [int(input()) for _ in range(9)]
smalls.sort()

for i in range(9):
    for j in range(i+1, 9):
        if sum(smalls) - (smalls[i] + smalls[j]) == 100:
            # 2개를 제외한 나머지 7개를 출력
            for k in range(9):
                if k != i and k != j:
                    print(smalls[k])
            exit()