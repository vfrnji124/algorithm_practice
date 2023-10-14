# 백준 17144: 미세먼지 안녕!
# R x C 격자판, r,c에는 값이 들어있음
# 공기청정기는 1번 열에만 있을 수 있고, 두 행을 차지한다.
# 공기청정기가 없는 칸에는 미세먼지가 있다.
# 1초 동안의 상황
# 1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
# (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
# 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는확산이 일어나지 않는다. -> if문으로 공청기, 공간 유무 확인
# 확산되는 양은 A[r][c]/5이고 소수점은 버린다. -> 확산 가능하면  연산
# (r, c)에 남은 미세먼지의 양은 A[r][c] - (A[r][c]/5)×(확산된 방향의 개수) 이다.
# 2. 공기청정기가 작동한다.
# 공기청정기에서는 바람이 나온다.
# 공기청정기 위쪽 칸의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

from collections import deque
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위쪽은 우상좌하, 공기청정기 아래쪽은 우하좌상
# 우선 방향벡터는 우상좌하 순서대로 정의 해놓고 필요할 때 순서 리스트 만들어서 바꿔쓰면 되겠다.
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 먼지가 있는 위치는 이중 for문을 사용해서 계속 찾을 수 밖에 없을 것 같다. 너무 많아.
# 한번만 써서 먼지위치랑 공청기 위치 리스트 만들어두자. 
# 공기청정기 위치는 두군데밖에 없으니까 이거는 리스트에 위치 저장해 놓자.

# 확산이 가능한 미세먼지 위치 리스트만 저장
dust = deque()
airfresher = []
def pos_detection():
    
    for r in range(R):
        for c in range(C):
            if A[r][c] == -1: 
                airfresher.append((r,c))
            elif A[r][c] != 0 and A[r][c] // 5 >= 1:
                dust.append((r,c))
                
def dust_diffusion():
    # 1. 먼지가 있는 위치 주변 탐색(칸 안에 있는지, 공청기가 있는지, 주변에 미세먼지가 있으면 합산하네, 
    #                    중요한 거는 현재 시간에 확산한 값이 옆에 값의 현재 시간 확산 계산에 영향을 주면 안됨.
    #                    확산되야 할 값을 저장해뒀다가 확산될 값들 전부 구한 다음에 합산해야할듯
    #                    주변 탐색-> 연산 -> 연산결과를 똑같은 테이블을 만들어서 저장? 리스트에 r,c,dust 순서의 튜플을 저장해두고
    #                    확산될 양 계산 다 한다음에 그 내용을 for문 돌면서 테이블에 반영시키면 되겠다. 먼지가 있던 위치는 바로 값 반영해도됨
    # 확산 연산 결과를 임시로 저장할 리스트, (r,c,확산될 양 저장)
    # global dust
    tmp_arr = []
    # 먼지 있는 위치 다 돌면서 확인하고, 이를 tmp_arr에 기록
    # dust_len = len(dust)
    # cnt = 0
    # while cnt < dust_len:
    while dust:
        dust_pos = dust.popleft()
        r, c = dust_pos
        diffsuable_area = 0
        # 네 방향 확인하면서 확산 가능한 영역 탐색, 먼지가 있던 칸의 먼지양 변화 계산에 반영
        # 5로 나눈 몫이 1 이하면 먼지가 사라지는 걸 여기서 처리해줘야한다.
        # 5보다 작은 영역은 변화가 없네...
        # if A[r][c] // 5 < 1:
        #     # 먼지 확산에 영향을 안주는거는 dust_pos에 포함시킬 필요가 없네..먼지 양은 어짜피 테이블에 저장되있고...
        #     # detection()에 반영!
        #     continue
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < R and 0 <= nc < C and A[nr][nc] != -1:
                tmp_arr.append((nr, nc, A[r][c] // 5))
                diffsuable_area += 1
        # tmp_arr에서 검출이 안되는 영역이 있을 것......
        A[r][c] -= (A[r][c] // 5) * diffsuable_area
        # if A[r][c] // 5 >= 1:
        #     dust.append((r,c))
        # cnt += 1
    # tmp_arr에 있는 내용을 돌면서 테이블에 반영
    for tmp in tmp_arr:
        r, c, d = tmp
        A[r][c] += d
    #     if A[r][c] // 5 >= 1:
    #         dust.append((r, c))
    # # (r,c)가 중복되서 들어간 영역이 있을 수 있으니 dust를 일단 set으로 중복 제거 해주도록 하자.
    # # 먼지 리스트를 업데이트
    # dust = deque(set(dust))

def machine_operation():
    u, d = airfresher[0][0], airfresher[1][0]
    # print(u, d)
    # 첫번째 열에 있는 먼지 공기청정기쪽으로 이동
    # 공기청정기 위칸부터 이동을 반영할 것이므로 idx는 1부터 시작
    idx = 1
    while u - idx > 0:
        A[u - idx][0] = A[u - idx - 1][0]
        idx += 1
    idx = 1
    while d + idx < R - 1:
        A[d + idx][0] = A[d + idx + 1][0]
        idx += 1
    # 첫행, 마지막행 이동
    idx = 0
    while idx < C - 1:
        A[0][idx] = A[0][idx + 1]
        A[-1][idx] = A[-1][idx + 1]
        idx += 1
    # 마지막열 있는거 움직임대로 이동
    idx = 0
    while idx < u:
        A[idx][-1] = A[idx + 1][-1]
        idx += 1
    idx = 0
    while idx <= R - d:
        A[-1 - idx][-1] = A[-2 - idx][-1]
        idx += 1
    # 공기청정기 옆칸은 마지막에 추가
    idx = C - 1
    while idx > 1:
        A[u][idx] = A[u][idx - 1]
        A[d][idx] = A[d][idx - 1]
        idx -= 1
    A[u][1] = 0
    A[d][1] = 0


t = 0
while t < T:
    pos_detection()
    dust_diffusion()
    machine_operation()
    t += 1
# print('---------------------')
# for row in A:
#     print(*row)
answer = 0
for row in A:
    answer += sum(row)
# 전부 다 더한 후 공기청정기 -1 * 2 보정
answer += 2
print(answer)

# print(dust)
# print(airfresher)