# 백준 1520: 내리막길
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
h = 0

def dfs(ey, ex):
    global h
    # 네방향 탐색하고, 이동이 가능하고 방문하지 않았으며, 높이가 낮다면, dfs. 
    if ey == m - 1 and ex == n - 1:
        h += 1
        print('-------------')
    for k in range(4):
        ny, nx = ey + dy[k], ex + dx[k]
        if 0 <= ny < m and 0 <= nx < n:
            if visited[ny][nx] == False and board[ey][ex] > board[ny][nx]:
                print(f'ny, nx:{ny}, {nx}, ey, ex: {ey}, {ex}')
                visited[ey][ex] = True
                dfs(ny, nx)
    visited[ey][ex] = False

visited[0][0] = True
dfs(0, 0)
print(h)