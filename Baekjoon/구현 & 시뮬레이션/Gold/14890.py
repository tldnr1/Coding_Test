import sys
input = sys.stdin.readline

N, L = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(N)]


def find_road(lines):
    res = 0
    for line in lines:
        # 경사로 설치 여부
        rail = [0] * N
        for i in range(N-1):
            # 차이 1칸 이내
            if abs(line[i]-line[i+1]) >= 2:
                break
            # 높이가 높아지는 경우
            if line[i] < line[i+1]:
                # 레일 설치된 적 없으면
                if i+1-L >= 0 and set(rail[i+1-L:i+1]) == {0}:
                    for x in range(i+1-L, i+1):
                        rail[x] = 1
                else:
                    break
            # 높이가 낮아지는 경우
            elif line[i] > line[i+1]:
                # 레일 설치된 적 없으면
                if i+L < N and set(rail[i+1:i+1+L]) == {0}:
                    for x in range(i+1, i+1+L):
                        rail[x] = 1
                else:
                    break
            # 끝까지 탐색한 경우
            if i == N-2:
                res += 1
    return res


def rotate(a):
    b = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            b[i].append(a[j][i])
    return b


print(find_road(lines) + find_road(rotate(lines)))
