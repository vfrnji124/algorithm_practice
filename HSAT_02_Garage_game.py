import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
spare = [[] for _ in range(n)]
board = [[] for _ in range(n)]
for i in range(3 * n):
    tmp = list(map(int, input().split()))
    
    for j in range(len(tmp)):
        if i < 2 * n:
            spare[j].append(tmp[j])
        else:
            board[j].append(tmp[j])
for i in range(len(spare)):
    spare[i] = spare[i][::-1]
for i in range(len(board)):
    board[i] = board[i][::-1]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def findNearSameColorCar(x, y, chk, board):
    # print('findNearSameColorCar----->')
    q = deque([(x, y)])
    chk[x][y] = 1
    color = board[x][y]
    board[x][y] = 0
    left, right = x, x 
    top, bottom = y, y
    while q:
        ex, ey = q.popleft()
        for k in range(4):
            nx, ny = ex + dx[k], ey + dy[k]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == color:
                board[nx][ny] = 0
                chk[nx][ny] = 1
                left = min(left, nx)
                right = max(right, nx)
                top = min(top, ny)
                bottom = max(bottom, ny)
                q.append((nx, ny))
    area = (right - left + 1) * (bottom - top + 1)
    return area, left, right, top, bottom

def makeNewBoard(board, spare, left, right, top, bottom):
    
    total_cnt = 0
    for x in range(left, right + 1):
        cnt = 0
        tmp = board[x][:top]
        for y in range(top, bottom + 1):
            if board[x][y] != 0:
                cnt += 1
                tmp.append(board[x][y])
        if bottom + 1 < n:
            tmp.extend(board[x][bottom+1:])
        zero_cnt = bottom - top + 1 - cnt        
        total_cnt += zero_cnt
        # print(f'tmp1:{tmp}')
        # print(zero_cnt)
        tmp.extend(spare[x][:zero_cnt])
        # print(f'tmp2:{tmp}')
        board[x] = tmp
        spare[x] = spare[x][zero_cnt:]
    return total_cnt
                
maxScore = 0
def dfs(turn, board, spare, score):
    global maxScore
    if turn == 3:
        maxScore = max(score, maxScore)
        return
    chk = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if chk[x][y] == 0:
                # print(f'turn:{turn}----->>>')
                copy_board = [board[i][:] for i in range(len(board))]
                area, left, right, top, bottom = findNearSameColorCar(x, y, chk, copy_board)
                copy_spare = [spare[i][:] for i in range(len(spare))]
                total_cnt = makeNewBoard(copy_board, copy_spare, left, right, top, bottom)
                # print(score, area, total_cnt)
                new_score = score + area + total_cnt
                # print('board')
                # print(copy_board)
                # print('spare')
                # print(copy_spare)
                # print(f'new_score:{new_score}')
                dfs(turn + 1, copy_board, copy_spare, new_score)

dfs(0, board, spare, 0)
print(maxScore)
# 해당 차례에서 선택할 수 있는 경우를 모두 탐색 -> 어떤걸 누르는지에 따라 그다음의 board, spare가 다르다. 그래서 복제해서 넘겨줘야 한다.
# 색 선택 -> 이때 없앨수 있는 차량 정리(차 대수, 새로운 맵, 이때 위에 남은 차량 필요->딥카피(copy패키지가 아니라 슬라이싱을 써야 한다.)) ,chk는 해당 차례에 공유(차량 선택 탐색때 필요) 다음차례엔 초기화