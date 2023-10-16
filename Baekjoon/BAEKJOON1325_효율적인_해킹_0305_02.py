# 백준 1325: 효율적인 해킹
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edge = [[] for _ in range(n+1)]
child_chk = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    edge[b].append(a)
    child_chk[a] = True

def bfs(start):
    chk = [False] * (n+1)
    q = deque([start])
    chk[start] = True
    cnt = 0
    while q:
        node = q.popleft()
        for i in edge[node]:
            if chk[i] == False:
                chk[i] = True
                cnt += 1
                q.append(i)
    return cnt

node_list=[]
maxv = 0
for i in range(1, n+1):
    if not child_chk[i]:
        val = bfs(i)
        if val > maxv:
            maxv = val
            node_list = [i]
        elif val == maxv:
            node_list.append(i)

node_list.sort()
for i in node_list:
    print(i, end=' ')

n, m = map(int, input().split())
edge = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    edge[b].append(a)
dfst = [0]*(n+1)
def dfs(start):
    if len(edge[start]) == 0:
        return 0
    else:
        result = 0
        for i in edge[start]:
            if dfst[1] != 0: 
                result += (dfst[i] + 1)
            else:
                result += (dfs(i) + 1)
        dfst[start] = result
        return dfst[start]

node_list = []
maxv = 0
for i in range(1, n+1):
    val = dfs(i)
    if val > maxv:
        node_list=[i]
        maxv = val
    elif val == maxv:
        node_list.append(i)

node_list.sort()
for num in node_list:
    print(num, end=' ')