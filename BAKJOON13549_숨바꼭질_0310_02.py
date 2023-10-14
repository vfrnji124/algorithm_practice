# 백준 13549: 숨바꼭질 3
from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize
max_size = 100001

N, K = map(int, input().split())
dist = [INF] * max_size
q = deque([N])
dist[N] = 0
while q:
    node = q.popleft()
    if 2 * node < max_size and dist[2 * node] > dist[node]:
        dist[2 * node] = dist[node]
        q.append(2 * node)
    if node - 1 >= 0 and dist[node - 1] > dist[node] + 1:  #부등호에 등호 안들어가서 틀렸다고 나옴
        dist[node - 1] = dist[node] + 1
        q.append(node - 1)
    if node + 1 < max_size and dist[node + 1] > dist[node] + 1:
        dist[node + 1] = dist[node] + 1
        q.append(node + 1)

print(dist[K])

# ✨ 입력
import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().split())
INF = 2147000000

# ✨ BFS
def BFS(N,K):
    dq = deque([])
    dq.append((0,N))
    ch_board = [INF] * (100001)
    ch_board[N] = 0
    while dq:
        val, node = dq.popleft()
        for x in [(1,node+1),(1,node-1),(0,node*2)]:
            if 0<=x[1]<100001:
                if ch_board[x[1]] > val+x[0]:
                    ch_board[x[1]] = val+x[0]
                    dq.append((ch_board[x[1]],x[1]))
    return ch_board[K]

# ✨ 출력
print(BFS(N,K))