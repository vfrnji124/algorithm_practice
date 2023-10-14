# 백준 5022: 연결
# 크기가 N x M인 비어있는 회로판, 두 점 A1,A2 / B1, B2를 전선을 이용해서 잇는다, 두 전선은 접하지 않아야 한다.
# 필요한 전선 길이의 최소값을 구하라.

# 한 점에서 다른 점까지의 최소길이를 구하는 문제 -> <bfs로 해결> (목적지에 도달했을 때 최소길이를 출력한다.)
# 한번 갔던 경로는 다른 경로탐색에서 방문하면 안된다. -> <완성된 최소길이 경로는 벽으로 처리해야 한다>
# -> 어느 노드로부터 방문하는건지 저장(path 리스트를 만들어야 한다.)
# 경로를 어느 점에 대해 먼저 완성하느냐에 따라 최소길이의 결과가 다르다. -> A를 먼저 BFS, B를 먼저 BFS, 두 결과중 최소값을 출력

import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
A, B = [], []
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
for i in range(4):
    x, y = map(int, input().split())
    if i < 2: A.append((y, x))
    else: B.append((y, x))

def bfs(A, B, visited, path):
    q = deque()
    sy, sx = A[0]  # 시작점
    fy, fx = A[1]  # 끝점
    
    # bfs 준비
    q.append(A[0]) # 큐에 시작점 추가
    visited[sy][sx] = 0 # 시작점 방문처리 및 거리 저장
    visited[B[0][0]][B[0][1]] = 0 # 다른 회로의 시작과 끝점은 방문하면 안되므로 방문처리
    visited[B[1][0]][B[1][1]] = 0 
    while q:
        ey, ex = q.popleft()
        # 큐에 들어있는 노드가 끝점이면 최소길이 반환
        if ey == fy and ex == fx:
            return visited[ey][ex]
        for k in range(4):
            ny, nx = ey + dy[k], ex + dx[k]
            if 0 <= ny <= M and 0 <= nx <= N:
                if visited[ny][nx] == -1:
                    visited[ny][nx] = visited[ey][ex] + 1
                    q.append((ny, nx))
                    path[ny][nx] = (ey, ex)
    return -1

def get_dist(A, B):
    visited = [[-1] * (N + 1) for _ in range(M + 1)]  # 최소 길이 계산
    path = [[(0, 0) for _ in range(N + 1)] for _ in range(M + 1)]  # 이전 노드 저장
    dist1 = bfs(A, B, visited, path)
    # path를 이용해서 끝점으로부터 방문경로를 역추적을 통해 이전 bfs의 최단경로를 방문처리
    visited = [[-1] * (N + 1) for _ in range(M + 1)]
    cy, cx = A[1]
    while True:
        visited[cy][cx] = 0
        if cy == A[0][0] and cx == A[0][1]:
            break
        cy, cx = path[cy][cx]
    dist2 = bfs(B, A, visited, path)
    return dist1, dist2

min_dist = INF
r1, r2 = get_dist(A, B)
if r1 != -1 and r2 != -1:
    min_dist = r1 + r2
r3, r4 = get_dist(B, A)
if r3 != -1 and r4 != -1:
    min_dist = min(min_dist, r3 + r4)

if min_dist == INF:
    print("IMPOSSIBLE")
else:
    print(min_dist)