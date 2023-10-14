from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

def bfs(y,x):
    q = deque([(y,x)])
    while q:
        ey, ex = q.popleft()
        chk[ey][ex] = True
        if map[ey][ex] != 0:
            for k in range(4):
                ny = ey + dy[k]
                nx = ex + dx[k]
                if 0 <= ny < N and 0 <= nx < M and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return 1

reps = 0 #년수 체크
# 주변 탐색을 위한 방향벡터 설정
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
node_chk = [[False] * M for _ in range(N)]

while 1:
    reps += 1
    for j in range(N):
        for i in range(M):
            if map[j][i] == 0 and node_chk[j][i] == False:
                for k in range(4):
                    nj = j + dy[k]
                    ni = i + dx[k]
                    if 0 <= nj < N and 0 <= ni < M:
                        if map[nj][ni] != 0:
                            map[nj][ni] -= 1
                            node_chk[nj][ni] = True
    
    chk = [[False]*M for _ in range(N)]
    cnt = 0
    for j in range(N):
        for i in range(M):
            if map[j][i] != 0 and chk[j][i] == False:
                chk[j][i] = True
                cnt += bfs(j,i)
    if cnt >= 2:
        break

# for j in range(N):
#     for i in range(M):
#         print(map[j][i], end='')
#     print()
print(reps)


# 시간초과 안나오는 답, 출처 : https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-2573-%EB%B9%99%EC%82%B0-BFS
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    seaList = []

    while q:
        x, y = q.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        if sea > 0:
            seaList.append((x, y, sea))
    for x, y, sea in seaList:
        graph[x][y] = max(0, graph[x][y] - sea)

    return 1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

while ice:
    visited = [[0] * m for _ in range(n)]
    delList = []
    group = 0
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if graph[i][j] == 0:
            delList.append((i, j))
    if group > 1:
        print(year)
        break
    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if group < 2:
    print(0)


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

ice = []
for j in range(N):
    for i in range(M):
        ice.append((j,i))
print(ice)