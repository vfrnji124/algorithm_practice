# 백준 19238: 스타트택시
# BFS를 이용해서 택시와 승객과의 거리를 구해서, 거리가 가장 가까운 손님먼저 태운다.
# 승객을 태우고 목적지까지 이동할만큼 연료가 남아있다면 운행이 가능하다.
# 운행이 불가능한 경우(-1을 출력)
# - 택시의 위치에서 승객까지 도달할 연료가 부족한 경우
# - 승객을 태우고 목적지까지 도달할 연료가 부족할 경우
# - 승객이나 목적지까지 가는 경로가 벽으로 막혀있는 경우
# 위의 경우를 제외하고 승객을 태우고 운행을 완료하면 승객의 위치부터 목적지까지의 거리 *2만큼 연료가 추가된다.

import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

# 입력 받기
n, m, fuel = map(int, input().split())  # n <= 20, m <= 20^2, fuel <= 500000
board = [list(map(int, input().split())) for _ in range(n)]
sy, sx = map(int, input().split())
startPosition = [sy - 1, sx - 1]
passengers = []  # [승객 위치, 목적지 위치]
for _ in range(m):
    ay, ax, by, bx = map(int, input().split())
    passengers.append([ay - 1, ax - 1, by - 1, bx - 1])

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 한 점에서 다른 점까지의 최소거리 -> BFS
def bfs(start:list):
    visited = [[-1] * n for _ in range(n)]
    sy, sx = start
    q = deque()
    q.append(start)
    visited[sy][sx] = 0
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny, nx = ey + dy[k], ex + dx[k]
            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == -1 and board[ny][nx] == 0:
                    q.append([ny, nx])
                    visited[ny][nx] = visited[ey][ex] + 1
    return visited

# 차량과 승객과의거리정보를 승객정보 맨 마지막에 저장하고 이를 기준으로 내림차순 정렬
def solve():
    global fuel
    global startPosition
    while passengers:
        carToPassengerDistanceTable = bfs(startPosition)
        for p in passengers:
            p.append(carToPassengerDistanceTable[p[0]][p[1]])
        # pprint(carToPassengerDistanceTable)
        passengers.sort(key=lambda x:(-x[4], -x[0], -x[1]))
        # print(passengers)

        py, px, fy, fx, dist = passengers.pop()
        if dist == -1:
            print(-1)
            return
        for p in passengers:
            p.pop()
        if fuel - dist < 0:
            print(-1)
            return
        # print(f'승객까지 위치:{dist}, 잔여 연료:{fuel}')
        fuel -= dist
        # print(f'승객을 태운 후 연료:{fuel}')
        passengerToDestinationDistanceTable = bfs([py, px])
        dist = passengerToDestinationDistanceTable[fy][fx]
        # print(f'목적지까지 가기 위한 연료:{dist}')
        if dist == -1:
            print(-1)
            return
        if fuel - dist < 0:
            print(-1)
            return
        fuel += dist
        startPosition = [fy, fx]
        # print(f'목적지에 도착한 후 연료: {fuel}')
    print(fuel)

solve()




