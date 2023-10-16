# 버튼을 특정 순서대로 누르면 특별한 식권을 얻을 수 있다.
# 비밀 메뉴가 나오는 조작법을 찾아냈다!
# 둘 모두에 포함된 일련의 조작법 중 가장 긴 것을 찾아야 한다.
# 연속된 부분 수열을 의미한다.
# 두 조작과정이 주어질 때, 둘 모두에 완전히 포함되는 조작과정 중 가장 긴것의 길이를 출력.
# 연속된 부분수열이었구나...
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [[0] * m for _ in range(n)]

longest = 0
for i in range(n):
    for j in range(m):
        if A[i] == B[j]:
            if i == 0 or j == 0:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + 1 
            if longest < C[i][j]:
                longest = C[i][j]

print(longest)
