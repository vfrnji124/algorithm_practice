import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
ID = [0]*(10**4+1)
table = [[0] * (m+2) for _ in range(n+2)]

def nearest(x, y):
    minD = 1000
    for i in range(1, n+1):
        for j in range(1, m+1):
            if table[i][j]:
                d = (x-i)*(x-i) + (y-j)*(y-j)
                if d < minD:
                    minD = d
    return minD

def assign(pid):
    maxD = 0
    # 모든 위치에 대해서 테스트를 해본다.
    for i in range(1, n+1):
        for j in range(1, m+1):
            if table[i][j] == 0 and table[i-1][j] == 0 and table[i+1][j] == 0 and table[i][j-1] == 0 and table[i][j+1] == 0:
                d = nearest(i, j)
                if d > maxD:
                    maxD = d
                    ID[pid] = [i, j]
    if maxD == 0:
        return False
    else:
        table[ID[pid][0]][ID[pid][1]] = 1
        return True


for i in range(q):
    inOut, pid = input().split()
    pid = int(pid)
    if inOut == 'In':
        if ID[pid] == 0:
            if assign(pid):
                print(f'{pid} gets the seat ({ID[pid][0]}, {ID[pid][1]}).')
            else:
                print('There are no more seats.')
        elif ID[pid] == 1:
            print(f'{pid} already ate lunch.')
        else:
            print(f'{pid} already seated.')
    elif inOut == 'Out':
        if ID[pid] == 0:
            print(f'{pid} didn\'t eat lunch.')
        elif ID[pid] == 1:
            print(f'{pid} already left seat.')
        else:
            print(f'{pid} leaves from the seat ({ID[pid][0]}, {ID[pid][1]}).')
            table [ID[pid][0]][ID[pid][1]] = 0
            ID[pid] = 1
