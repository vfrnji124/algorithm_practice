from collections import defaultdict
L, Q = map(int, input().split())

dishInfo = defaultdict(list)
customerInfo = defaultdict(list)
dishCount = 0
customerCount = 0
event = []

for _ in range(Q):
    command = list(input().split())

    if command[0] == '100':
        t1 = int(command[1])
        x1 = int(command[2])
        name = command[3]
        event.append((t1, '1+'))
        dishInfo[name].append([t1, x1])
        # 시간초과 원인!
        # 아래 명령을 반복문에서 밖으로 빼야한다. in 명령이 Q반복문 안에서 해당 블록이 돌아갈 때마다 실행되게 할게 아니라 마지막에 한번만 실행되게 해야 한다.
        # eatTime = -1
        # if name in set(customerLocation.keys()):
        #     t2 = customerLocation[name][0]
        #     x2 = customerLocation[name][1]
        #     eatTime = t1 + (x2 - x1 + L) % L
        #     # 음식이 사라지는 이벤트를 추가
        #     event.append((eatTime, '1-'))
        #     customerLocation[name][2] -= 1
        #     outTime = max(customerLocation[name][-1], eatTime)
        #     customerLocation[name][-1] = outTime

        #     if customerLocation[name][2] == 0:
        #         event.append((outTime, '2-'))
        
    elif command[0] == '200':
        t2 = int(command[1])
        x2 = int(command[2])
        name = command[3]
        event.append((t2, '2+'))
        customerInfo[name] = [t2, x2]
        # 위와 같은 마찬가지 이유로 시간초과가 발생하니, in문을 최소한으로 쓸 수 있도록 구조를 설계해야 한다.     
        # outTime = -1
        # if name in set(dishLocation.keys()):
        #     for dish in dishLocation[name]:
        #         t1 = dish[0]
        #         x1 = dish[1]
        #         eatTime = t2 + (x2 - ((x1 + (t2-t1)) % L) + L) % L
        #         dish[-1] = eatTime
        #         event.append((eatTime, '1-'))
        #         outTime = max(eatTime, outTime)
        # if orderCount == 0:
        #     event.append((outTime, '2-'))

    elif command[0] == '300':
        t = int(command[1])
        event.append((t,'3'))

names = set(dishInfo.keys())

# 음식이 소비되는 이벤트 정리하기
for name in names:
    t2 = customerInfo[name][0]
    x2 = customerInfo[name][1]
    # 맨 마지막에 음식이 소비되는 시간이 손님이 나가는 시각
    outTime = -1
    for dish in dishInfo[name]:
        t1 = dish[0]
        x1 = dish[1]
        # 음식이 들어온 시점이 먼저인 경우
        if t1 < t2:
            # x2: t2시간에 손님의 위치, (x1 + (t2-t1)) % L : t2시간에서 음식의 위치,
            # 음식위치 3 손님위치 1이면 1-3 = -2  + 6  = 4 % 6
            eatTime = t2 + (x2 - ((x1 + (t2 - t1)) % L) + L) % L
        # 음식이 손님이 들어온 이후에 만들어진 경우
        elif t1 > t2:
            eatTime = t1 + (x2 - x1 + L) % L
        event.append((eatTime, '1-'))
        outTime = max(outTime, eatTime)
    event.append((outTime, '2-'))


event.sort()

for _, cmd in event:
    if cmd == '1+':
        dishCount += 1
    elif cmd == '1-':
        dishCount -= 1
    elif cmd == '2+':
        customerCount += 1
    elif cmd == '2-':
        customerCount -= 1
    else:
        print(customerCount, dishCount)