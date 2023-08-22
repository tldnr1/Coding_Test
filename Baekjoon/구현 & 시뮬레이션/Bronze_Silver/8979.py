import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ranking = dict()
for _ in range(n):
    x, a, b, c = map(int, input().split())
    ranking[x] = (a, b, c)

sorted_ranking = sorted(ranking.items(), key=lambda item: item[1], reverse=True)

rank = 1
next_rank = 1
for i in range(n-1):
    next_rank += 1
    if sorted_ranking[i][0] == k:
        break

    r1, r2 = sorted_ranking[i][1], sorted_ranking[i+1][1]
    if r1[0] == r2[0] and r1[1] == r2[1] and r1[2] == r2[2]:
        continue
    else:
        rank = next_rank

print(rank)
