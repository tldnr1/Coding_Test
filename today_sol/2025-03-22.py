# 2024 카카오 겨울 인턴십 1번 문제 - 가장 많이 받은 선물
def solution(friends, gifts):
    friends_dict = {v: i for i, v in enumerate(friends)}
    l = len(friends)
    p = [0] * l # 선물지수
    answer = [0] * l

    gift_table = [[0] * l for i in range(l)]
    for i in gifts:
        a, b = i.split()
        gift_table[friends_dict[a]][friends_dict[b]] += 1
    for i in range(l):
        p[i] = sum(gift_table[i]) - sum([k[i] for k in gift_table])

    for i in range(l):
        for j in range(l):
            if gift_table[i][j] > gift_table[j][i]:
                answer[i] += 1
            elif gift_table[i][j] == gift_table[j][i]:
                if p[i] > p[j]:
                    answer[i] += 1
    return max(answer)