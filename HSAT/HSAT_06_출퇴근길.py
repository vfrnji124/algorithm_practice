import sys
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
adjR = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adjR[y].append(x)
s, t = map(int, input().split())

# 입력 확인
print(f'n, m: {n}, {m}')
print(f'adj: {adj}')
print(f'adjR: {adjR}')
print(f's, t: {s}, {t}')

# 집에서도 도달이 가능하고, 해당 노드에서 출근길에서 도달 가능해야 한다. -> 집에서 도달가능한 노드
# 퇴근길에서도 도달이 가능하고, 해당 노드에서 다시 집으로 도달이 가능해야 한다. -> 회사에서 도달 가능한 노드
# 노드에서 퇴근길, 노드에서 출근길로 도달 가능한 노드를 찾으려면, 간선의 방향을 바꿔서 찾으면 한점에서 찾으면 된다.

def dfs(now, adj, visit):
    if visit[now] == 1:
        return
    visit[now] = 1
    for neighbor in adj[now]:
        dfs(neighbor, adj, visit)
    return

fromS = [0] * (n+1)
dfs(s, adj, fromS)
fromT = [0] * (n+1)
dfs(t, adj, fromT)
toS = [0] * (n+1)
dfs(s, adjR, toS)
toT = [0] * (n+1)
dfs(t, adjR, toT)

count = 0
for i in range(1, n+1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        count += 1
print(count)
