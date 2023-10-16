# 차량이 들어오는 최대 경우의 수가 20만, 시간은 10**9까지 들어올 수 있다.
# for문을 1~10**9까지 돌려고 하면 시간초과가 난다.
# 차량에 대해서 반복하고, 차량이 있는 시간대의 교차로 상황만 다루려고 해야 한다.
# 이를 고려해서 알고리즘을 설계해야 한다.
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
cross = [deque() for _ in range(4)]
cross_map={'A':0, 'B':1, 'C':2, 'D':3}
for i in range(n):
    t, w = input().split()
    cross[cross_map[w]].append((i, int(t)))

carInfo = [-1 for _ in range(n)]
curr_time = 0

# 차량이 교차로에 있는지 체크, 교차로에 일단 차량을 다 넣어놓은 상태기 때문에 특정 시점에 차량이 존재하는지를 체크하기 위해
# 네 방향에 차의 존재 여부를 0,1로 체크할 수 있는 리스트를 사용함.
is_waiting = [0, 0, 0, 0]
# 교차로에 차량이 한대라도 있으면 계속 반복을 진행한다.
while cross[0] or cross[1] or cross[2] or cross[3]:
    # 교차로에 넣어 놓은 차량 중 시간상 앞서는 차량을 찾는다.
    min_time = 10**9
    for i in range(4):
        if cross[i]:
            # 0번은 차량번호, 1번은 차량이 교차로에 도착한 시간
            time = cross[i][0][1]
            # 시간상 빨리 온 차량으로 최소시간 갱신
            min_time = min(min_time, time)
            # 차량이 도착한 시간이 진행시간보다 이르거나 같다면, 해당 교차로에 차량이 있는 상태니까 이를 교차로
            if time <= curr_time:
                is_waiting[i] = 1
    # 교차로에 몇대가 대기중인지
    num_waiting_cars = sum(is_waiting)
    # 교차로가 가득 찬 상태이면 더이상 진행이 안되므로 탈출
    if num_waiting_cars == 4:
        break
    # curr_time 교차로에 차량이 없다면, 시간을 차량이 오기 시작하는 시간으로 점프
    if num_waiting_cars == 0:
        curr_time = min_time
        continue
    # 그 시간에 교차로에 차량이 있으면서, 오른쪽 차선에 차량이 없는 경우에만 차량을 탈출시킬 수 있다.
    for i in range(4):
        if is_waiting[i] and not is_waiting[(i-1)%4]:
            # 차량번호만 필요하고 차량이 교차로를 탈출한 시간은 curr_time에서 반환할 것.
            idx, _ = cross[i].popleft()
            carInfo[idx] = curr_time
            is_waiting[i] = 0
    # is_waiting을 초기화를 해야하네?
    # for i in range(4):
    #     is_waiting[i] = 0
    curr_time += 1
print(*carInfo, sep='\n')