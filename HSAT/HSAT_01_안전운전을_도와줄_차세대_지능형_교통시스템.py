# 입력 받기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, T = map(int, input().split())
traffic = [[list(map(int, input().split())) for _ in range(N)] for _ in range(N)]
visited = [[0] * N for _ in range(N)]
# [1,2,3,4]
# > V < ^ 순서
# d_mark = ['>', 'V', '<', '^']
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
# signal = [in, out]
# 갈수 있냐 아니냐를 숫자로 표기하는 게 아니라 0과 1을 이용해서 표현할 수도 있다.
# signal[신호번호][들어오는방향][나가는방향] = 0(불가능), 1(가능)
# 근데 내가 한 방법도 되는 방법이긴 해.
signal = [[], 
[0, [0,1,3]], [3, [2,3,0]], [2,[1,2,3]], [1,[0,1,2]],
[0, [0,3]], [3, [2,3]], [2, [1,2]], [1, [1,0]],
[0, [0,1]], [3, [3,0]], [2, [2,3]], [1, [1,2]]]

# signalInfo = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(13)]
# for i in range(4):
#     signalInfo[i+1][i][(i+1)%4] = 1
#     signalInfo[i+1][i][(i+2)%4] = 1
#     signalInfo[i+1][i][(i+3)%4] = 1

#     signalInfo[i+5][i][(i+2)%4] = 1
#     signalInfo[i+5][i][(i+3)%4] = 1

#     signalInfo[i+9][i][(i+1)%4] = 1
#     signalInfo[i+9][i][(i+2)%4] = 1

# junction = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
# junction[0][0][1] = 1
# junction2 = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
# visit = [[0 for _ in range(N)] for _ in range(N)]
# def update(time, row, col, inDir, outDir, junction, junction2):
#     signalNow = traffic[row][col][time % 4]
#     if signalInfo[signalNow][inDir][outDir]:
#         if outDir == 0 and col != 0:
#             junction2[row][col-1][2] = 1
#             visit[row][col-1] = 1
#         elif outDir == 1 and row != N - 1:
#             junction2[row+1][col][3] = 1
#             visit[row+1][col] = 1
#         elif outDir == 2 and col != N - 1:
#             junction2[row][col+1][0] = 1
#             visit[row][col+1] = 1
#         elif outDir == 3 and row != 0:
#             junction2[row-1][col][1] = 1
#             visit[row-1][col] = 1
#     return 

# for time in range(T):
#     for row in range(N):
#         for col in range(N):
#             for inDir in range(4):
#                 if junction[row][col][inDir]:
#                     for outDir in range(4):
#                         update(time, row, col, inDir, outDir, junction, junction2)
#                     junction[row][col][inDir] = 0
#     junction, junction2 = junction2, junction


# t시간에 도달할 수 있는 차들의 위치정보가 있어야 한다. -> bfs

def dfs(y, x, t, direction):
    if t == T:
        return
    sig_list = traffic[y][x]
    t_sig = signal[sig_list[t % 4]]
    in_dir = t_sig[0]
    out_dir_list = t_sig[1]

    if direction == in_dir:
        for k in out_dir_list:
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                visited[ny][nx] = 1
                dfs(ny, nx, t+1, k)

    # t일때 신호의 in 방향이 교차로의 진입방향과 같은지 체크,
        # 같으면 신호 방향으로 이동 가능한지 확인.
            # 이동 가능하면 해당 경로로 이동하고 t+1하고 진입방향 넣어서 dfs
            # 이동 불가능하면 그냥 t+1해서 대기
        # 다르면 t + 1해서 대기

visited[0][0] = 1
dfs(0, 0, 0, 3)
answer = 0
for row in visited:
    answer += sum(row)
print(answer)