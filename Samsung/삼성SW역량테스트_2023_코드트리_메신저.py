# 문제 정리
# 사내 메신저 구조는 모든 노드의 자식이 2개 이하인 이진트리로 되어있다.
# 최상단 노드는 회사의 메인 채팅방이고, 그 밑의 자식노드는 부서별 채팅방

# 1. 사내 메신저 준비
# 0 ~ N번까지 N+1개의 채팅방
# 회사의 메인 채팅방 제외 각 채팅방은 부모 채팅방이 있다.
# 메인 채팅방의 번호는 항상 0이다.
# 각 채팅방의 부모 채팅방 번호는 parents라는 이름으로 주어진다.
# 메인 채팅방은 부모가 없기 때문에, parent값이 주어지지 않는다.
# parents값은 1번부터 N번까지 순서대로 주어진다.
#  ex) N = 8, parents[0]:1의 parent
# 각 채팅방은 authority를 갖고 있다.
# c번 채팅방에서 메세지를 보내면 채팅방의 상위 채팅방들에게 알림이 가게 된다.
# authority_c만큼 위로 올라가며, 알림을 보내게 된다.
# 이 값은 authority라는 배열로 주어진다.
# 0번 채팅방은 메인 채팅방이어서 parent, authority, 알림망 설정과 관련이 없다.

# 2. 알림망 설정 ON/OFF
# 처음 모든 채팅방의 알림망 설정은 켜져있다.
# 이 기능이 작동되면, c번 채팅방의 알림망 설정이 On 상태면 Off로 변경/Off상태면 On으로 바꿔준다.
# 알림망 설정이 Off되면 자기 자신을 포함한 아래에서 올라온 모든 알림을 더이상 위로 올리지 않는다.

# 3. 권한 세기 변경
# c번 채팅방의 권한세기를 power로 변경한다.

# 4. 부모 채팅방 교환
# c1, c2번 채팅방의 부모를 서로 바꾼다. c1과 c2의 채팅방은 트리 내에서 depth가 같음을 가정한다.

# 5. 알림을 받을 수 있는 채팅방 조회
# c번 채팅방까지 알림이 도달할 수 있는 서로 다른 채팅방의 수를 출력한다.

# Q번에 거쳐 명령을 순서대로 진행하며, 알맞은 답을 출력하는 프로그램을 작성하라.

# 입력
# 첫째줄에 채팅방 수 N과 명령 수 Q가 주어진다.
# 사내 메신저 준비
# 100 p1~pN a1~aN 각 채팅방의 부모 채팅방 번호와, 초기 권한 세기가 주어진다.
# 이 명령은 항상 첫번째 명령으로 주어진다.

# 알림망 설정 On/Off
# 200 c 형태로 주어지고, c번 채팅방의 알림망 설정이 On 상태면 Off, Off 상태면 On으로 바꾼다.

# 권한 세기 변경
# 300 c power 형태로 주어지고, c번 방의 권한 power를 변경한다.

# 부모 채팅방 교환
# 400 c1 c2 형태로 주어진다.

# 알림받을 수 있는 채팅방 수 조회
# 500 c

N, Q = map(int, input().split())
notification = [[0] * 21 for _ in range(N+1)]
onOffList = [True] * (N+1)

def updateAuthority(node, prevPower, newPower):
    notification[node][prevPower] -= 1
    notification[node][newPower] += 1
    curNode = node
    i = 0
    while curNode:
        i += 1
        if not onOffList[curNode]:
            break
        parent = parents[curNode]
        if newPower - i >= 0:
            notification[parent][newPower-i] += 1
        if prevPower - i >= 0:
            notification[parent][prevPower-i] -= 1
        if newPower - i <= 0 and prevPower - i <= 0:
            break
        curNode = parent

def toggleOnOff(isOn, node):
    curNode = node
    tmpNode = node
    i = 0
    while tmpNode:
        i += 1
        parent = parents[tmpNode]
        for power in range(i,21):
            if isOn:
                notification[parent][power-i] += notification[curNode][power]
            else:
                notification[parent][power-i] -= notification[curNode][power]
        if not onOffList[parent]:
            break
        tmpNode = parent

for _ in range(Q):
    Query = list(map(int, input().split()))
    command = Query[0]

    if command == 100:
        parents = [0] + Query[1:N+1]
        authorities = [0]
        for a in Query[N+1:]:
            authorities.append(min(20, a))

        for i in range(1, N+1):
            power = authorities[i]
            notification[i][power] += 1
            curNode = i
            while power and curNode:
                power -= 1
                parent = parents[curNode]
                notification[parent][power] += 1
                curNode = parent
        
    elif command == 200:
    # on/off 하게 되면 부모노드에 저장된 값에 자기 노드를포함한 자기 하위노드의 개수를 뺌
        c = int(Query[1])
        isOn = not onOffList[c]
        onOffList[c] = isOn
        toggleOnOff(isOn, c)
        

    elif command == 300:
        # 노드의 파워가 변경되면 해당 노드가 전파될수 있는 노드에 정보 업데이트

        c = int(Query[1])
        newPower = min(20, int(Query[2]))
        prevPower = authorities[c]
        authorities[c] = newPower
        updateAuthority(c, prevPower, newPower)

            
    elif command == 400:
        c1, c2 = map(int, Query[1:])
        isOn1 = onOffList[c1]
        isOn2 = onOffList[c2]
        
        if isOn1:
            toggleOnOff(False, c1)
        if isOn2:
            toggleOnOff(False, c2)
        parents[c1], parents[c2] = parents[c2], parents[c1]
        if isOn1:
            toggleOnOff(True, c1)
        if isOn2:
            toggleOnOff(True, c2)

    elif command == 500:
        c = int(Query[1])
        print(sum(notification[c])-1)
