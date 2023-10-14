# 백준 20057: 마법사 상어와 토네이도
import sys
input = sys.stdin.readline
# 토네이도는 표 정가운데부터 시작해서 반시계방향으로 회전해나간다.
# 격자 밖으로 나간 모래의 양을 출력
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 토네이도 이동 여부 확인, 토네이도 이동 구현에 필요함
chk = [[False] * N for _ in range(N)]
# 방향벡터 설정, 토네이도 방향에 맞게 반시계 방향으로 설정
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
# 토네이도의 영향을 받는 좌표 설정, 비율은 키로, 방향을 값으로 설정

per_1 = [(-1, 1), (1, 1)], [(-1, -1), (-1, 1)], [(-1, -1), (1, -1)], [(1, -1), (1, 1)]
per_2 = [(-2, 0), (2, 0)], [(0, -2), (0, 2)], [(-2, 0), (2, 0)], [(0, -2), (0, 2)]
per_5 = [(0, -2)], [(2, 0)], [(0, 2)], [(-2, 0)]
per_7 = [(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, 0), (1, 0)], [(0, -1), (0, 1)]
per_10 = [(-1, -1), (1, -1)], [(1, -1), (1, 1)], [(-1, 1), (1, 1)], [(-1, -1), (-1, 1)]
percentage = {1:per_1, 2:per_2, 5:per_5, 7:per_7, 10:per_10}
start = N // 2
# 1. 토네이도 이동 구현

r, c = start, start
chk[r][c] = True
direction = 0
answer = 0
while True:
    # 토네이도가 이동할 위치 받기
    nr = r + dr[direction]
    nc = c + dc[direction]    
    if chk[nr][nc] == True:
        direction -= 1
        nr = r + dr[direction]
        nc = c + dc[direction]
    # 토네이도가 다 돌아서 (0, -1)을 가리키면 탈출
    if nc == -1 :
        break
    # print('nr, nc:', nr, nc)
    chk[nr][nc] = True

    # 격자 안인지 확인할 것.(모래 이동량 계산 후 배열에 더해줄 때 확인하면 됨)
    # 이동시켜야 할 양이 격자 밖이면 answer에 저장
    # 토네이도 이동에 따른 모래 이동 구현
    # 이동하는 방향의 모래양 확인
    sands = arr[nr][nc]
    arr[nr][nc] = 0
    minus_val = 0
    # 비율에 맞게 모래 뿌리고 뿌린 모래양만큼 sand에서 차감
    for p, pos_list in percentage.items():
        val = int(sands * (p / 100))
        # print('val:', val)
        if val > 0:
            # print('p, pos_list:', p, pos_list)
            for pos in pos_list[direction]:
                y, x = pos
                ny = nr + y
                nx = nc + x
                minus_val += val
                if 0 <= ny < N and 0 <= nx < N:
                    arr[ny][nx] += val
                else:
                    answer += val
    sands -= minus_val
    ny = nr + dr[direction]
    nx = nc + dc[direction]
    if 0 <= ny < N and 0 <= nx < N:
        arr[ny][nx] += sands
    else:
        answer += sands
    # r, c 업데이트
    r = nr
    c = nc
    direction = (direction + 1) % 4
    # print('nr, nc answer:', answer)
    # for row in arr:
    #     print(*row)
print(answer)