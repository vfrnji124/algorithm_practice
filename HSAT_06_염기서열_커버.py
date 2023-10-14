import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dna = []
for _ in range(n):
    dna.append(list(input().strip()))


superDNA = [None for _ in range(2**n)]
superDNA[0] = ['.']*m

def merge(dna1, dna2):
    # 두 염기서열을 합칠 수 없으면 null list를 사용
    if dna1 == [] or dna2 == []:
        return []
    dna = []
    # 두 dna의 각 자리를 비교
    for i in range(m):
        if dna1[i] == '.':
            dna.append(dna2[i])
        elif dna2[i] =='.':
            dna.append(dna1[i])
            # 둘다 어드밴티지면 아래 경우에 포함됨!, 따로 경우를 안만들어도 되지.
        elif dna1[i] == dna2[i]:
            dna.append(dna1[i])
        # 조합이 불가능하면 null list, 중간까지 만들다가 안되는 경우 빈 리스트를 반환해야하므로 이 경우를 꼭 포함시켜야 함.
        else:
            return []
    return dna
        


def genSuperDNA(index):
    loc = 0
    tempIndex = index
    # 비트의 맨 오른쪽 1의 위치를 찾음. -> DP를 이용한 방법
    # 1110은 1100과 0010으로 쪼개서 계산할 수 있다.
    while tempIndex % 2 == 0:
        tempIndex = tempIndex//2
        loc += 1
    # dna로 한가지의 염기서열과, 초염기서열 만들어뒀던 것과 결합해서 더 많이 결합된 초염기서열을 만듦
    superDNA[index] = merge(dna[loc], superDNA[index-2**loc])

# n개로 만들 수 있는 부분집합을 비트로 표현: n자리의 이진 비트
# 0번은 만들어져있으므로 1번부터 계산.
for i in range(1, 2**n):
    genSuperDNA(i)
print(superDNA)