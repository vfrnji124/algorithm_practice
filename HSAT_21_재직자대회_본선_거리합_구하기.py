# 무조건 알아둬야 하는 문제!
# 모든 노드가 이어진 경우, 모든 노드에 대해 노드와 노드간의 거리를 구하는 문제 -> 플로이드-와샬
# 근데 플로이드 와샬의 시간복잡도는 반복문을 세번 도는거기 때문에. n^3, n의 사이즈가 작을때만 사용이 가능한 알고리즘
# 그런데 이 문제의 경우 n이 20만까지 올 수 있기 때문에 사용할 수가 없다.

# 모든 노드에 대해 dfs를 사용하려고 하면 -> O(V(V+E)) = O(n(n+n-1)) ~= O(n^2) -> 역시 이방법도 시간복잡도가 초과됨

# 루트 노드에 대해 모든 노드와의 거리의 합을 구한다.
# 그리고 각 노드에 대해 서브트리의 사이즈를 구한다.
# 리프노드들은 1이고, 리프노드 세대로 구성된 루트노드의 서브트리 사이즈는 리프노드의 서브트리사이즈의 합에 자기자신을 포함해서 4가 된다.
# 루트노드의 하위 리프노드에서부터 접근하려면, 루트에서 리프로 가는 모든 노드에 대한 비용이 총 비용에 추가된다.
# 반대로 해당 하위 노드의 하위 노드들은 루트노드로부터 그 노드까지 가는 비용만큼은 줄어들게 될 것이다. 

import sys
input = sys.stdin.readline

# 트리구조가 주어졌을 때 하나의 노드를 루트노드로 잡았을 때 그 하위 노드의 서브트리 갯수를 구하는 과정
def dfs1(current, parent):
    subtreeSize[current] = 1
    for i in range(len(node[current])):
        child = node[current][i][0]
        weight = node[current][i][1]
        if child != parent:
            # dfs1을 먼저 call을 하고 계산
            dfs1(child, current)
            distSum[current] += distSum[child] + subtreeSize[child]*weight
            subtreeSize[current] += subtreeSize[child]
    return

def dfs2(current, parent):
    for i in range(len(node[current])):
        child = node[current][i][0]
        weight = node[current][i][1]
        if child != parent:
            # 계산을 마친 다음에 dfs2를 call
            distSum[child] = distSum[current] + weight*(N-2*subtreeSize[child])
            dfs2(child, current)
    return

N = int(input())
subtreeSize = [0]*(N+1)
node = [[] for _ in range(N+1)]
distSum = [0] * (N+1)
for i in range(N-1):
    x, y, t = map(int, input().split())
    node[x].append([y, t])
    node[y].append([x, t])

dfs1(1, 1)
dfs2(1, 1)
for i in range(1, N+1):
    print(distSum[i])