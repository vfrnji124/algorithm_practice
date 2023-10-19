   
l, n, q = map(int, input().split())

# 체스판(0: 빈칸, 1: 함정, 2: 벽)
board = [list(map(int, input().split())) for _ in range(l)]
knightAlive = set(i for i in range(1, n+1))
is_moved = [False] * (n+1)
total_dmg = [0] * (n+1)
dmg = [0] * (n+1)
r = [0] * (n+1)
c = [0] * (n+1)
h = [0] * (n+1)
w = [0] * (n+1)
k = [0] * (n+1)
nr = [0] * (n+1)
nc = [0] * (n+1)
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(n):
    id = i + 1
    ri, ci, hi, wi, ki = map(int, input().split())
    r[id] = ri-1
    c[id] = ci-1
    h[id] = hi
    w[id] = wi
    k[id] = ki

# # 기사 이동(DFS)
def canMoveKnight(id, d):
    #기사의 위치를 체크
    is_moved[id] = True
    nr[id] = r[id] + dy[d]
    nc[id] = c[id] + dx[d]
    # 기사가 이동했을 때 맵 밖으로 나가면 이동 불가능
    if nr[id] < 0 or nr[id] + h[id] - 1 >= l or nc[id] < 0 or nc[id] + w[id] - 1 >= l:
        return False
    
    # 기사를 움직일 수 있는지 체크(밀리는 기사가 밀려지는지를 체크)
    for j in range(nr[id], nr[id] + h[id]):
        for i in range(nc[id], nc[id] + w[id]):
            # 이동한 위치에 벽이 있으면 이동이 불가능
            if board[j][i] == 2:
                return False
            if board[j][i] == 1:
                dmg[id] += 1
    
    for i in range(1, n+1):
        # 체력이 없는 나이트면 컨티뉴
        # print('살아있는 기사:', knightAlive)
        if i not in knightAlive:
            continue
        if is_moved[i]:
            continue
            # 이렇게 관리할 필요가 없구나, 그냥 종류별로 리스트를 만들면 되네. 그 종류의 데이터에 대해 id로 구분되니까.
            # 그냥 이런식의 클래스별로 관리하면 정의하는 과정에서 코드만 길어지네..
            # 탐색 대상인 기사가 현재 선택된 기사의 행과 겹치지 않으면 밀리는 기사가 아님
        if r[i] > nr[id] + h[id] - 1 or nr[id] > r[i] + h[i] - 1:
            continue
        if c[i] > nc[id] + w[id] - 1 or nc[id] > c[i] + w[i] - 1:
            continue
        if not canMoveKnight(i, d):
            return False

    return True    

def push(id, d):
    # 초기화
    # global knightAlive
    print('살아있는기사:', knightAlive)
    for i in range(1, n+1):
        is_moved[i] = False
        dmg[i] = 0
        nr[i] = r[i]
        nc[i] = c[i]
    
    # 이동이 가능하면 갱신
    if canMoveKnight(id, d):
        killedKnight = set()
        for i in range(1, n+1):
            r[i] = nr[i]
            c[i] = nc[i]
            if id != i:
                k[i] -= dmg[i]
                total_dmg[i] += dmg[i]
            if k[i] <= 0:
                killedKnight.add(i)
        knightAlive -= killedKnight

for _ in range(q):
    i, d = map(int, input().split())
    if i not in knightAlive:
        continue
    push(i, d)

answer = 0
for i in knightAlive:
    answer += total_dmg[i]
print(answer)