# 백준 20058: 마법사 상어와 파이어스톰
from collections import deque
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
table_size = pow(2,N)
A = [list(map(int, input().split())) for _ in range(table_size)]
stage = list(map(int, input().split()))

# 방향벡터(하, 우, 상, 좌)
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def rotation(start_y, start_x, N):
    move = 2 * N - 1
    ey, ex = start_y, start_x
    er, ec = start_y + move, start_x 
    tmp = deque()
    # print('ey, ex:', ey, ex)
    # print('er, ec:', er, ec)
    yxdirection = 0
    rcdirection = 1
    # 값의 이동을 위해 임시 큐에 값 저장
    for i in range(move):
        tmp.append(A[ey + dr[yxdirection] * i][ex + dc[yxdirection] * i])
    # print('ey, ex:', ey, ex)
    # print('tmp:', tmp)
    # 값을 반시계 방향으로 이동    
    for _ in range(3):
        for i in range(move + 1):
            if i == move:
                ey += dr[yxdirection] * i
                ex += dc[yxdirection] * i
                er += dr[rcdirection] * i
                ec += dc[rcdirection] * i
                yxdirection += 1
                rcdirection += 1
            else:    
                A[ey + dr[yxdirection] * i][ex + dc[yxdirection] * i] = A[er + dr[rcdirection] * i][ec + dc[rcdirection] * i]
    # ey += dr[yxdirection] * i
    # ex += dc[yxdirection] * i
    # yxdirection += 1
    # print('왜 yxidrection out of range?', yxdirection)
    for i in range(move):
        A[ey + dr[yxdirection] * i][ex + dc[yxdirection] * i] = tmp.popleft()

    # for k in range(4):
    #     for _ in range(move):
    #         ny = ey + dr[k]
    #         nx = ex + dc[k]
    #         A[ey][ex] = A[ny][nx]
    #         ey = ny
    #         ex = nx
    # A[ey][ex + 1] = tmp


# 회전까지 구현 완료!

# 얼음 녹는거 처리하기
# 얼음이 녹는 위치 적어두기

def ice_chk():
    melt_pos = deque()
    for j in range(table_size):
        for i in range(table_size):
            ice_count = 0
            for k in range(4):
                nj = j + dr[k]
                ni = i + dc[k]
                if 0 <= nj < table_size and 0 <= ni < table_size and A[nj][ni] != 0:
                    ice_count += 1
            if ice_count < 3:
                melt_pos.append((j, i))
    print('melt pos:', melt_pos)
    while melt_pos:
        r, c = melt_pos.popleft()
        A[r][c] = max(0, A[r][c] - 1)
    print('--------------------')
    for row in A:
        print(*row)

# L의 갯수만큼 단계 실행
for L in stage:
    for j in range(0, table_size, pow(2, L)):
        for i in range(0, table_size, pow(2, L)):
            for l in range(pow(2, L) // 2):
                print('l:',l )
                rotation(j + l, i + l, pow(2, L) // 2 - l)
    ice_chk()

# 연결된 얼음덩어리의 갯수를 구하기 위한 자료구조 정의
chk = [[False] * table_size for _ in range(table_size)]
sum_answer = 0
count_answer = 0
for row in A:
    sum_answer += sum(row)
print(sum_answer)

for j in range(table_size):
    for i in range(table_size):
        if chk[j][i] == True:
            continue
        if A[j][i] > 0:
            q = deque([(j, i)])
            while q:
                ej, ei = q.popleft()
                chk[ej][ei] = True
                if A[ej][ei] > 0:
                    count_answer += 1
                for k in range(4):
                    nj = ej + dr[k]
                    ni = ei + dc[k]
                    if 0 <= nj < table_size and 0 <= ni < table_size and chk[nj][ni] == False:
                        chk[nj][ni] = True
                        if A[nj][ni] > 0: 
                            q.append((nj, ni))
print(count_answer)