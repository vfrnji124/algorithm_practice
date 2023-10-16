# 세트를 만드는데 해당 레벨의 갯수가 모자라면 중간 레벨의 갯수를 가져오게 하면 된다.
# 순서대로 탐색해야 하는데, 정렬이 가능하다면, 이분 탐색을 이용해 시간복잡도를 logN으로 줄일 생각을 해야 한다.
import sys
input = sys.stdin.readline

def test(testSets):
    # S배열이 들어가는 대신에 그냥 변수 하나를 이용해도 된다.
    S = [0] * n
    S[0] = C[0]
    for i in range(n-1): # 총 n세트가 있지만 맨 마지막은 i+1이 생기면 안되기 때문에 n-1까지 돌아야 한다.
        # S[i] : C[i]에 D[i-1]에서 넘어올 수 있는 것을 넘겨와서 더한 것을 저장할 것.
        if S[i] >= testSets:
            # 목표하고자 하는 테스트셋을 만들고도 S[i] 남는 정도면 D[i]번에 있는 것 전부를 C[i]번에 안붙이고 C[i+1]에 붙여도 충분함.
            S[i+1] = C[i+1] + D[i]
            # S[i]에서 D[i]번에 있는 것을 끌어와서 더해와야 필요한 테스트셋의 갯수를 만족하는 경우.
        elif S[i] + D[i] >= testSets:
            S[i+1] = C[i+1] + (S[i] + D[i] - testSets) # 테스트셋을 위해 필요한 정도 빼고는 그 다음세트에 넘겨준다.
            # 뒤에 있는 걸 끌어와도 테스트셋을 못채운 경우가 되므로 이 testSets만큼을 만드는 것은 불가능. 중간보다 낮은값에서 다시 이분탐색
        else:
            return False
    # 전부 다 돌고나서 맨 마지막에 있는 것까지 테스트셋을 만족하면 이는 가능한 케이스.
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