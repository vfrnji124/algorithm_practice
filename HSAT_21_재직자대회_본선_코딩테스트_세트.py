# 세트를 만드는데 해당 레벨의 갯수가 모자라면 중간 레벨의 갯수를 가져오게 하면 된다.
# 순서대로 탐색해야 하는데, 정렬이 가능하다면, 이분 탐색을 이용해 시간복잡도를 logN으로 줄일 생각을 해야 한다.
import sys
input = sys.stdin.readline

def test(testSets):
    S = [0] * n
    S[0] = C[0]
    for i in range(n-1):
        if S[i] >= testSets:
            S[i+1] = C[i+1] + D[i]
        elif S[i] + D[i] >= testSets:
            S[i+1] = C[i+1] + (S[i] + D[i] - testSets)
        else:
            return False
    if S[n-1] >= testSets:
        return True
    else:
        return False

def bSearch(start, end):
    if start == end:
        return start
    mid = (start+end+1)//2
    if test(mid):
        return bSearch(mid, end)
    else:
        return bSearch(start, mid-1)

n, t = map(int, input().split())
for i in range(t):
    C = [0] * n
    D = [0] * (n-1)
    temp = list(map(int, input().split()))
    for i in range(n-1):
        C[i] = temp[2*i]
        D[i] = temp[2*i+1]
    C[n-1] = temp[2*(n-1)]
    print(bSearch(0, 2*10**12))