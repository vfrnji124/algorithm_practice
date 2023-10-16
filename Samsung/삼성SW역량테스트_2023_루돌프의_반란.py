rudolph_dy = [0, -1, -1, -1, 0, 1, 1, 1]
rudolph_dx = [-1, -1, 0, 1, 1, 1, 0, -1]
santa_dy = [-1, 0, 1, 0]
santa_dx = [0, 1, 0, -1]

# 충돌 구현
def bump(dy, dx, santaID, y, x, power, isBump):
    if isBump:
        santaScore[santaID] += power
    ny, nx = y + power * dy, x + power * dx
    if 0 <= ny < N and 0 <= nx < N:
        if field[ny][nx] == 0:
            field[ny][nx] = santaID
            santaLocation[santaID] = (ny, nx)
        else:
            santaID2 = field[ny][nx]
            field[ny][nx] = santaID
            santaLocation[santaID] = (ny, nx)
            bump(dy, dx, santaID2, ny, nx, 1, False)
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

# 1. 소 이동
# 1) 소와 가장 가까운 유저 선택
m = 0
while playingSanta and m < M:
    outSanta = set()
    pickedSanta = 0
    ry, rx = rudolphLocation
    distanceList = []
    for santaID in playingSanta:
        sy, sx = santaLocation[santaID]
        rudolphDistance = (ry - sy)**2 + (rx - sx)**2
        distanceList.append([rudolphDistance, -sy, -sx, santaID])
    distanceList.sort()
    pickedSanta = distanceList[0][3]

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
        bump(nry-ry, nrx-rx, santaID, nry, nrx, C, True)
    else:
        field[nry][nrx] = -1
    rudolphLocation = (nry, nrx)
    
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
                bump(sy-nsy, sx-nsx, santaID, nsy, nsx, D, True)
                break
            # 빈칸이면 이동
            elif field[nsy][nsx] == 0:
                field[nsy][nsx] = santaID
                santaLocation[santaID] = (nsy, nsx)
                field[sy][sx] = 0
                break
    isKnockDown = isKnockDown_next
    isKnockDown_next = [0] * (P+1)

    playingSanta -= outSanta
    for i in playingSanta:
        santaScore[i] += 1
    m += 1

print(*santaScore[1:])