import sys
from collections import defaultdict, deque
input = sys.stdin.readline

plain = deque(list(input().strip()))
cipher = deque(list(input().strip()))
grid = [[''] * 5 for _ in range(5)]
alpahbet_locations = dict()
code = 65
for j in range(5):
    for i in range(5):
        while cipher and cipher[0] in alpahbet_locations.keys():
            cipher.popleft()
        if cipher:
            c = cipher.popleft()
            grid[j][i] = c
            alpahbet_locations[c] = (j, i)
        else:
            while chr(code) in alpahbet_locations.keys():
                code += 1
                if code == 74: code += 1
            grid[j][i] = chr(code)
            alpahbet_locations[chr(code)] = (j, i)
# 65:A, 74:J 90:Z
def doEncryption(string):
    s1, s2 = string[0], string[1]
    s1y, s1x = alpahbet_locations[s1]
    s2y, s2x = alpahbet_locations[s2]
    if s1y == s2y:
        print(grid[s1y][(s1x+1)%5], end='')
        print(grid[s2y][(s2x+1)%5], end='')
    elif s1x == s2x:
        print(grid[(s1y+1)%5][s1x], end='')
        print(grid[(s2y+1)%5][s2x], end='')
    else:
        print(grid[s1y][s2x], end='')
        print(grid[s2y][s1x], end='')

def makeCharGroup():
    start = ''
    while len(start) != 2:
        if not plain:
            start += 'X'
            break
        if start != plain[0]:
            start += plain.popleft()
        else:
            if start != 'X':
                start += 'X'
            else:
                start += 'Q'
    return start

while plain:
    twoChar = makeCharGroup()
    doEncryption(twoChar)
    




# 2.암호화하기(행, 열 같은거 확인, 둘다 다르면 열만 바꿈)
# 두 글자의 행번호 체크
# 두 글자의 열번호 체크
# else: 두글자의 열을 바꿔서 출력