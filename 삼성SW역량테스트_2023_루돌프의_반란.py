from collections import deque
from pprint import pprint
rudolph_dy = [0, -1, -1, -1, 0, 1, 1, 1]
rudolph_dx = [-1, -1, 0, 1, 1, 1, 0, -1]
santa_dy = [-1, 0, 1, 0]
santa_dx = [0, 1, 0, -1]

# 최단거리 탐색
def bfs(y, x, visited):
    q = deque([(y, x)])
    visited[y][x] = 0
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny, nx = ey + santa_dy[k], ex + santa_dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == -1:
                    visited[ny][nx] = visited[ey][ex] + 1
                    q.append((ny, nx))
    # 산타가 이동할 때의 루돌프와의 최단 경로 구하기

# bfs로 구할게 아니네...

# 충돌 구현
def bump(dy, dx, santaID, y, x, power):
    santaScore[santaID] += power
    ny, nx = y + power * dy, x + power * dx
    if 0 <= ny < N and 0 <= nx < N:
        if field[ny][nx] == 0:
            field[ny][nx] = santaID
            santaLocation[santaID] = (ny, nx)
        else:
            playerID2 = field[ny][nx]
            field[ny][nx] = santaID
            santaLocation[santaID] = (ny, nx)
            interaction(dy, dx, playerID2, ny, nx)
    else:
        outSanta.add(santaID)
        santaLocation[santaID] = (-1, -1)

# 상호 작용
def interaction(dy, dx, santaID, y, x):
    ny, nx = y + dy, x + dx
    if 0 <= ny < N and 0 <= nx < N:
        if field[ny][nx] == 0:
            field[ny][nx] = santaID
            santaLocation[santaID] = (ny, nx)
        else:
            santaID2 = field[ny][nx]
            field[ny][nx] = santaID
            santaLocation[santaID] = (ny, nx)
            interaction(dy, dx, santaID2, ny, nx)
    else:
        outSanta.add(santaID)
        santaLocation[santaID] = (-1, -1)

N, M, P, C, D = map(int, input().split())
santaScore = [0] * (P+1)
playingSanta = set(i for i in range(1, P+1))
field = [[0] * N for _ in range(N)]
santaLocation = [(-1, -1) for _ in range(P+1)]
cy, cx = map(int, input().split())
rudolphLocation = (cy-1, cx-1)
field[cy-1][cx-1] = -1
for _ in range(P):
    i, r, c = map(int, input().split())
    santaLocation[i] = (r-1, c-1)
    field[r-1][c-1] = i
isKnockDown = [0] *(P+1)
isKnockDown_next = [0]*(P+1)
# print('초기 field->')
# pprint(field)
# 1. 소 이동
# 1) 소와 가장 가까운 유저 선택
m = 0
while playingSanta and m < M:
    outSanta = set()
    pickedSanta = 0
    minDist = 2 * (N ** 2) + 1
    ry, rx = rudolphLocation
    for santaID in playingSanta:
        sy, sx = santaLocation[santaID]
        rudolphDistance = (ry - sy)**2 + (rx - sx)**2
        if minDist > rudolphDistance:
            minDist = rudolphDistance
            pickedSanta = santaID
        elif minDist == rudolphDistance:
            if sy > santaLocation[pickedSanta][0]:
                pickedSanta = santaID
            elif sy == santaLocation[pickedSanta][0] and sx > santaLocation[pickedSanta][1]:
                pickedSanta = santaID

    # 돌진 대상 산타에게 가장 가까이 가는 경로를 탐색해서 그 경로로 이동
    minDist = 2*N**2 + 1
    ahead = -1
    for k in range(8):
        nry, nrx = ry + rudolph_dy[k], rx + rudolph_dx[k]
        if 0 <= nry < N and 0 <= nrx < N:
            dist = (nry - santaLocation[pickedSanta][0]) ** 2 + (nrx - santaLocation[pickedSanta][1]) ** 2
            if minDist > dist:
                minDist = dist
                ahead = k
    nry, nrx = ry + rudolph_dy[ahead], rx + rudolph_dx[ahead]
    field[ry][rx] = 0
    # 위치에 산타가 있으면
    if field[nry][nrx] != 0:
        santaID = field[nry][nrx]
        field[nry][nrx] = -1
        isKnockDown[santaID] = 1
        isKnockDown_next[santaID] = 1
        bump(nry-ry, nrx-rx, santaID, nry, nrx, C)
    else:
        field[nry][nrx] = -1
    rudolphLocation = (nry, nrx)
    # print(f'{m}에서 소 이동->')
    # pprint(field)
    
    # 2. 산타 이동
    for santaID in sorted(list(playingSanta)):
        if isKnockDown[santaID]:
            continue
        sy, sx = santaLocation[santaID]
        curDist = (sy-nry) ** 2 + (sx-nrx) ** 2
        ahead = []
        # 현재 위치보다 거리가 짧아지면 리스트에 거리값과 방향을 추가
        # 거리값으로 정렬하고, 그때 그 방향으로 향할 때 해당 칸에 뭐가 있는지 확인하면 됨.
        # 산타가 이동가능한 네 방향중 가장 짧은 거리의 값과 그때의 방향을 탐색
        for k in range(4):
            nsy, nsx = sy + santa_dy[k], sx + santa_dx[k]
            if 0 <= nsy < N and 0 <= nsx < N:
                dist = (nry - nsy) ** 2 + (nrx - nsx) ** 2
                if curDist > dist:
                    ahead.append((dist, k))
        # 위에서 선택된 방향중에 이동이 가능한지 여부 탐색
        for _, k in sorted(ahead):
            nsy, nsx = sy + santa_dy[k], sx + santa_dx[k]
            # 루돌프가 있으면 루돌프와 박치기
            if field[nsy][nsx] == -1:
                field[sy][sx] = 0
                isKnockDown_next[santaID] = 1
                bump(sy-nsy, sx-nsx, santaID, nsy, nsx, D)
                break
            # 빈칸이면 이동
            elif field[nsy][nsx] == 0:
                field[nsy][nsx] = santaID
                santaLocation[santaID] = (nsy, nsx)
                field[sy][sx] = 0
                break
    isKnockDown = isKnockDown_next
    isKnockDown_next = [0] * (P+1)
    # print(f'{m}에서 산타 이동->')
    # pprint(field)

    playingSanta -= outSanta
    for i in playingSanta:
        santaScore[i] += 1
    m += 1
    # print(f'{m} score: {santaScore}')
print(*santaScore[1:])