import sys
from collections import deque
input = sys.stdin.readline

def solve():
    t = int(input())

    for _ in range(t):
        p = input().strip()
        
        # N 버리기
        input() 
        
        arr_str = input().strip()

        if arr_str == "[]":
            n = deque()
        else:
            n = deque(map(int, arr_str[1:-1].split(',')))
            
        is_error = False
        is_reversed = False
        
        # R, D 명령 순회
        for cmd in p:
            if cmd == 'R':
                is_reversed = not is_reversed
            
            elif cmd == 'D':
                if len(n) == 0:
                    is_error = True
                    break
                else:
                    if not is_reversed:
                        n.popleft() # 정방향
                    else:
                        n.pop() # 역방향
        
        # 결과 출력
        if is_error:
            print("error")
        else:
            if is_reversed:
                n.reverse()
            print('[' + ','.join(map(str, n)) + ']')

solve()