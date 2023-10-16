import sys
input = sys.stdin.readline

def calIndegree(dag):
    indegree = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(1, dag[i][0]+1):
            indegree[dag[i][j]] += 1
    return indegree

def tsort(dag):
    # 인디그리 계산
    indegree = calIndegree(dag)
    # 인디그리가 0인것부터 차례로 지워나가고 이를 지우면서 하위노드의 인디그리를 1 감소
    stack = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            stack.append(i)
    ordering = []
    while stack:
        node = stack.pop()
        ordering.append(node)
        for i in range(1, dag[node][0]+1):
            child = dag[node][i]
            indegree[child] -= 1
            if indegree[child] == 0:
                stack.append(child)
    return ordering

n, k = map(int, input().split())
dag = [[0]] + [list(map(int, input().split())) for _ in range(n)]
ordering = tsort(dag)

traffic = [0]*(n+1)
traffic[1] = k
for i in range(n):
    node = ordering[i]
    request = traffic[node]
    if dag[node][0] == 0:
        continue
    quotient = request // dag[node][0]
    remainder = request % dag[node][0]
    for j in range(1, dag[node][0]+1):
        child = dag[node][j]
        traffic[child] += quotient
        if j < remainder + 1:
            traffic[child]

print(*traffic[1:])