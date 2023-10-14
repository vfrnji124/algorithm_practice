# 백준 16234: 인구 이동(bfs를 이용해서 문제를 품)
from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

# 두 도시의 인구수 차이로 연합을 이룰 수 있는거 체크
# 연합이 된다고 하면 갯수 체크하고 위치 정보 저장해야겠다.

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(start):
    q = deque([start])
    chk[start[0]][start[1]] = True
    cnt = 0
    number = 0
    union_list = []
    while q:
        y, x = q.popleft()
        number += land[y][x]
        cnt += 1
        union_list.append((y, x))
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < N and chk[ny][nx] == False:
                if L <= abs(land[ny][nx] - land[y][x]) <= R:
                    chk[ny][nx] = True
                    q.append((ny, nx))
    if len(union_list) == 1:
        return False
    else:
        # print('union_list:', union_list, len(union_list))
        after = int(number / len(union_list))
        for nation in union_list:
            land[nation[0]][nation[1]] = after
        return True

days = 0
while 1:
    chk = [[False] * (N) for _ in range(N)]
    run = False
    for j in range(N):
        for i in range(N):
            if chk[j][i] == True:
                continue
            run |= bfs((j, i))
            # print('y, x:', j, i)
            # print(f'run {days}:', run)
    if run:
        days += 1
        # print(days,'일')
        # for row in land:
        #     print(*row)
    else:
        print(days)
        break 
