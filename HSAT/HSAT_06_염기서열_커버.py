# HSAT 6회: 염기서열 커버

# <문제 요약>
# DNA 염기서열은 4종류의 핵염기가 일자로 연결된 가닥 : a, c, g, t
# N개의 좋은 염기서열과, 좋은 염기서열의 길이는 M
# 좋은 염기서열은 어떤 문자든 올 수 있는 와일드카드(.)를 몇 개 가질 수 있다.
# 좋은 염기서열의 조건을 만족하는 염기서열을 초염기서열이라고 한다.
# 좋은 염기서열마다 초염기서열을 만드는 것이 아닌, 하나의 초염기서열이 여러 그룹의 좋은 염기서열을 커버하고자 한다.
# 주어진 모든 좋은 염기서열을 커버하기 위한 최소한의 초염기서열의 개수를 구하라.

# <아이디어>
# 1. n과 m이 작다. -> O(2**n)도 가능하겠다고 판단해야 한다. 2**15 ~= 32000
# 2. 하나의 초 염기서열로 커버가 되는 게 몇 개인지는 나열하면 알 수 있다. 그 다음에 두개 이상을 생각해보자.
# 3. 초 염기서열의 총 갯수 : 임의의 좋은 염기서열을 합칠 수가 있는 것이므로 가능한 모든 부분집합을 구하는 문제 -> 2**N개
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dna = [input().strip() for _ in range(n)]

# 초염기서열을 담을 자료구조, 맨 앞은 공집합이므로 와일드카드처리
superDNA = [None] * (2**n)
superDNA[0] = '.' * m

# 염기서열의 조합인 초염기서열을 n 비트의 숫자로 표현 : n자리 2진수로 표현
# 만약 4비트이고 1010이면 첫번째와 세번째의 좋은 염기서열을 커버하고, 두번째 네번째 염기서열은 커버할 수 없는 초염기서열을 표현

# 들어오는 index의 맨 오른쪽에 나오는 1의 위치를 찾아 loc에 저장한다.
# 만약 1110이면 이를 1100, 0010으로 나누기 위해서 위치를 찾는다. 이렇게 분리된 숫자는 index보다 작은 숫자이고 이 인덱스일 때 초염기서열은 찾은 상태
# 두개의 값을 합하면 superDNA[index]를 구할 수 있다.
def genSuperDNA(index):
    # O(n+m)
    loc = 0
    tempIndex = index
    while tempIndex % 2 == 0: # O(n)
        tempIndex //= 2
        loc += 1
    superDNA[index] = merge(dna[loc], superDNA[index - 2**loc]) # O(m)

# 염기서열 두 개를 입력받아 합치는 함수, 이미 두개의 염기서열이 합쳐져서 합칠 수 없는 염기서열이면 빈 리스트를 반환한다.
# 예: 1101의 초염기서열이 가능한지 확인하려고 1100과 0001 두개를 merge 하는데 이미 1100이 불가능하다고 판별이 난 상황이다.
# 그럼 1100이 빈 문자열일테고, 이 경우 하나라도 빈 문자열이면 초 염기서열이 불가능한 것이므로 빈 문자열을 반환하게 한다.
def merge(dna1, dna2):
    # O(m)
    # 하나라도 초염기서열이 만들어질 수 없는 거라면 결과도 초염기서열이 만들어질 수 없다.
    if dna1 == '' or dna2 == '':
        return ''
    dna = ''
    for i in range(m):
        if dna1[i] == '.':
            dna += dna2[i]
        elif dna2[i] == '.':
            dna += dna1[i]
        elif dna1[i] == dna2[i]:
            dna += dna1[i]
        else:
            # 합칠 수 없는 경우
            return ''
    return dna

# 0번은 계산할 필요가 없으니 1번부터 계산
# 초염기서열이 가능한 것 찾기
for i in range(1, 2**n):
    # O(2**n(n+m)) ~= 2**15
    genSuperDNA(i) # O(n+m)

# 초염기서열이 한개로 표현이 안되는 빈 문자열들이 초염기서열 몇개가 필요한지 계산해야 한다.
# 110110 -> 염기서열 네 개를 합한 것, 이 중 1을 뽑는 것의 가짓수 = 2**4 , (0000, 1111)을 빼고 나열하면 2**4 - 2
# 1이 있는 비트만 넣었다 뺐다 하면서 조합을 찾는 것. 110110에서 0은 무시하고 네자리만 이용해서 모든 조합을 찾는다.
# 이를 위해 1이 있는 부분의 자리수를 저장하고, 숫자를 탐색할 때 2**자릿수를 더해나가면 된다.
# 나눌 수 있는 모든 부분집합을 나눠서 DP를 돌린다.

def genAnswer(index):
    # 인덱스에 해당하는 answer가 초기값과 다르다면 계산이 되었던 것이므로 탈출 조건으로 사용.
    # DP구현이라 재귀를 쓰기 때문에 탈출 조건 필요
    if answer[index] < n+1:
        return answer[index]

    # 1이 있는 자리의 위치를 기억해야 하므로 이를 저장할 자료구조 선언
    bit1 = []
    number1 = number2 = 0
    tempIndex = index
    for i in range(n):
        # 마지막 자리가 1이면 해당 자리수를 bit1에 append
        if tempIndex % 2 == 1:
            bit1.append(i)
            number2 += 2 ** i
        tempIndex //= 2

    # 1이 있는 위치의 갯수 크기의 리스트를 생성
    digit = [0] * len(bit1)

    # 1을 더하는 연산
    # bit 길이 -1인 이유 : num1과 num2가 대칭이어서 num1에 나왔던 수가 num2에도 나오므로, 2를 나눠줘도 모든 경우가 다 고려됨.
    for i in range(1, 2**(len(bit1) - 1)):
        for j in range(len(bit1)):
            
            # 뒷자리가 1인 경우 : 뒤의 값이 1이면 0으로 바뀌고 처음 나오는 0이 1로 바뀌고, 그 앞은 그대로
            if digit[j] == 1:
                digit[j] = 0
                temp = 2 ** bit1[j]
                number1 -= temp
                number2 += temp
            # 뒷자리가 0인 경우: 뒤의 값을 1로 바꿔주면 됨
            else:
                digit[j] = 1
                temp = 2 ** bit1[j]
                number1 += temp
                number2 -= temp
                break
        temp = genAnswer(number1) + genAnswer(number2)

        if answer[index] > temp:
            answer[index] = temp
    return answer[index]
# 초기값을 n+1로 설정한 이유, 염기서열의 갯수가 n개이기 때문에 최대 필요한 염기서열이 n개를 넘을 수 없음.
answer = [n+1] * (2**n)
answer[0] = [0]

for i in range(1, 2**n):
    # 빈 문자열이 아니면 하나의 초염기서열로 커버가 가능한 경우이므로, 해당 index의 answer는 1
    if superDNA[i] != '':
        answer[i] = 1
    else:
        genAnswer(i)

# 모든 비트가 다 1일 경우의 값
print(answer[2**n-1])