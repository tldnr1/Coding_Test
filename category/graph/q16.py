# Q16 - 연구소
from itertools import combinations
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
before = []  # 초기 맵
for _ in range(n):
    before.append(list(map(int, input().split())))

# 방향 벡터
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# BFS로 바이러스 전파
def spread_virus():
    q = deque()
    after = deepcopy(before)

    for i in range(n):
        for j in range(m):
            if after[i][j] == 2:  # 바이러스 발견 시 큐에 삽입
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and after[nx][ny] == 0:
                after[nx][ny] = 2
                q.append((nx, ny))
    
    # 안전 영역 계산
    return sum(row.count(0) for row in after)

# 빈 칸 좌표만 추출
empty_spots = [(i, j) for i in range(n) for j in range(m) if before[i][j] == 0]

# 모든 경우의 수에서 3개의 벽을 설치
for comb in combinations(empty_spots, 3):
    for x, y in comb:
        before[x][y] = 1  # 벽 설치

    # 바이러스 확산 후 안전 영역 계산
    result = max(result, spread_virus())

    for x, y in comb:
        before[x][y] = 0  # 벽 복원

print(result)