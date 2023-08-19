king, stone, n = input().split()
k = [ord(king[0]) - 64, int(king[1])]
s = [ord(stone[0]) - 64, int(stone[1])]
n = int(n)

# 문제 체스판 오른쪽 90도 회전해서 생각
move = {
    'R': [1, 0],
    'L': [-1, 0],
    'B': [0, -1],
    'T': [0, 1],
    "RT": [1, 1],
    "LT": [-1, 1],
    "RB": [1, -1],
    "LB": [-1, -1]
}

for _ in range(n):
    m = input()
    dx, dy = move[m]
    # king, stone 다음 위치
    nk = [k[0] + dx, k[1] + dy]
    ns = s
    if nk == s:
        ns = [s[0] + dx, s[1] + dy]
    # 범위 밖 무시 (1 ~ 8)
    if nk[0] < 1 or nk[0] > 8 or nk[1] < 1 or nk[1] > 8 or \
            ns[0] < 1 or ns[0] > 8 or ns[1] < 1 or ns[1] > 8 :
        continue
    k = nk
    s = ns

print(chr(k[0]+64) + str(k[1]))
print(chr(s[0]+64) + str(s[1]))
