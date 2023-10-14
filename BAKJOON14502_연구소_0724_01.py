# 백준 14502: 연구소
# 문제 요약
# 바이러스(2)는 상하좌우 방향의 빈 공간(0)으로 확산
# 바이러스는 벽(1)을 통과하지 못함
# 맵에서 벽을 반드시 3개를 세워야 한다
# 바이러스가 퍼지지 않는 안전영역의 갯수가 최대인 값을 구하라

# 1. 아이디어
# 바이러스가 퍼지는 영역은 BFS를 이용해서 구할 수 있다.
# 벽을 세우는 위치는 규칙이 없으므로 완전탐색을 통해서 구현해야 한다.

# 2. 자료구조
# graph : 입력으로 제공되는 맵 저장
# queue : BFS를 구현하기 위한 큐
# answer : 안전영역의 최대값을 저장할 변수

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
GRAPH = [list(map(int, input().split())) for _ in range(N)]
EMPTY_ARIAS = []
dy = [0,1,0,-1] 
dx = [1,0,-1,0]
ANSWER = 0

from collections import deque
from itertools import combinations
import copy

# 큐 선언 및 큐에 시작노드 삽입
queue = deque()
for j in range(N):
    for i in range(M):
        if GRAPH[j][i] == 2:
            queue.append((j, i))
        elif GRAPH[j][i] == 0:
            EMPTY_ARIAS.append((j, i))

MAKE_WALL = (combinations(EMPTY_ARIAS,3))
for wall in MAKE_WALL:
    COPY_GRAPH = copy.deepcopy(GRAPH)
    COPY_QUEUE = copy.deepcopy(queue)
    for y, x in wall:
        COPY_GRAPH[y][x] = 1

    while COPY_QUEUE:
        y, x = COPY_QUEUE.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if COPY_GRAPH[ny][nx] == 0:
                    COPY_GRAPH[ny][nx] = 2
                    COPY_QUEUE.append((ny, nx)) 

    # 맵에서 0인 영역의 갯수 세기
    cnt = 0
    for row in COPY_GRAPH:
        cnt += row.count(0)
        ANSWER = max(cnt, ANSWER)

print(ANSWER)