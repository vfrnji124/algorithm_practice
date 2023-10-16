import sys
input = sys.stdin.readline

numBuyer = int(input())
offer = [] # [size, payment, buyerID]
for i in range(numBuyer):
    temp = list(map(int, input().split()))
    for j in range(temp[0]):
        offer.append([temp[2 * j + 1], temp[2 * j + 2], i + 1])

numScenario = int(input())
temp = list(map(int, input().split()))
scenario = [] # [target_revenue, targetID, size]
for i in range(numScenario):
    scenario.append([temp[i], i+1])

# 2차원 배열을 sort하면 맨 앞의 원소를 기준으로 sort를 하게 됨.
# sort해야 하는 이유. size를 증가시켜가면서 매출액이 얼마나 증가하는지 체크
offer.sort()
scenario.sort()

revenue = 0
# 특정 시나리오에서 모든 바이어들이 어떤 차를 살 수 있는지 담기 위한 리스트.
# 시나리오에서 제시한 차량보다 작은 사이즈 중에서 가장 많은 비용을 지불할 수 있는 경우로 계속 갱신한다음에.
# 확인이 끝나면, 리스트에 들어간 값의 합을 구하도록 한다.
# 사이즈를 정렬을 했기 때문에, 점점 더 큰 숫자가 나오므로, 작은 숫자에 대응되는 과정은 동일하므로 이전과정을 반복할 필요는 없다.
buyerPayment = [0 for _ in range(numBuyer + 1)]
print(buyerPayment)
sIndex = 0
for i in range(len(offer)):
    size, payment, buyerID = offer[i]
    # print(f'ID:{buyerID}, length:{len(buyerPayment)}')
    if payment > buyerPayment[buyerID]:
        revenue += -buyerPayment[buyerID] + payment
        buyerPayment[buyerID] = payment
    while(sIndex < numScenario and scenario[sIndex][0] <= revenue):
        scenario[sIndex].append(size)
        sIndex += 1
while(sIndex < numScenario):
    scenario[sIndex].append(-1)
    sIndex += 1
scenario.sort(key=lambda x:x[1])
for i in range(len(scenario)):
    print(scenario[i][-1], end=' ')

