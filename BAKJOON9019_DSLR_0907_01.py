# 백준 9019: DSLR
# 최소한의 명령어를 이용하라 -> 최소한의 경로 구하기와 유사한 문제 -> BFS임을 떠올려야 한다.
import sys
input = sys.stdin.readline
from collections import deque

t = int(input())  # 테스트케이스 입력

def command(num, case):  # 각 명령에 대해 구현
    if case == 'D':
        # n을 두배로 바꾼다. 결과가 만을 넘어가면 만으로 나눈 나머지를 결과로 한다.
        return (int(num) * 2) % 10_000
    elif case == 'S':
        # n에서 1을 뺀 결과를 레지스터에 저장, n이 0이라면 9999가 저장된다.
        return (int(num)-1) % 10_000 # -1을 10000으로 나눈 나머지를 구하면 9999가 나온다.
    elif case == 'L':
        # n의 각 자릿수를 왼편으로 회전시켜서 그 결과를 레지스터에 저장
        # 레지스터에 저장된 네자릿수는 왼편부터 d2, d3, d4, d1
        tmp = num // 1000
        return num % 1000 * 10 + tmp
    elif case == 'R':
        # n의 각 자릿수를 오른편으로 회전시켜서 그 결과를 레지스터에 저장
        # 레지스터에 저장되는 네지릿수는 d4, d1, d2, d3
        tmp = num % 10
        return num // 10 + tmp * 1000
    
# for문을 돌면서 다음의 경우를 확인
# BFS에서 dx, dy의 역할
order_list = ['D', 'S', 'L', 'R']

def bfs(a, b, visited):
    #a와 빈 문자열을 q에 넣어주고 시작.
    q = deque()
    q.append([a, ""])
    # a는 방문처리
    visited[a] = 1
    while q:
        num, case = q.popleft()
        if num == b:
            print(case)
            break
        # D,S,L,R을 적용해보고 가능한 숫자를 구한다.
        for order in order_list:
            n_case = command(num, order)
            if visited[n_case] == 0:
                # 가능한 숫자가 있다면, 가능한 숫자와 가능하게 한 문자를 처음""로 시작한 문자열 뒤에 붙여준다.
                q.append([n_case, case+order])
                visited[n_case] = 1

for _ in range(t):
    # 조건에서 10000미만이라고 했으니, 10000으로 초기화한다.
    visited = [0 for _ in range(10000)]
    a, b = map(int, input().split())
    bfs(a, b, visited)