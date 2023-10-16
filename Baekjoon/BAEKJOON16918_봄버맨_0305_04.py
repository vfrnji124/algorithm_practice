# 백준 16918: 봄버맨
import sys
input = sys.stdin.readline

r,c,n=map(int, input().split())
map=[list(input().strip()) for _ in range(r)]
if n%2 == 0:
    for j in range(r):
        for i in range(c):
            print('O', end='')
        print()

elif n%4==3:
    chk=[[False]*c for _ in range(r)]

    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    for j in range(r):
        for i in range(c):
            if map[j][i] == 'O' and chk[j][i] == False:
                map[j][i] = '.'
                chk[j][i] = True
                for k in range(4):
                    nj = j + dy[k]
                    ni = i + dx[k]
                    if 0<=nj<r and 0<=ni<c:
                        if chk[nj][ni] == True:
                            map[nj][ni] = '.'
                        elif map[nj][ni] == '.':
                            chk[nj][ni] = True


            elif map[j][i] =='.' and chk[j][i] == False:
                map[j][i] = 'O'
                chk[j][i] = True
    for m in map:
        for i in m:
            print(i, end='')
        print()

elif n%4==1:
    for m in map:
        for i in m:
            print(i, end='')
        print()

#비교해보자...
import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
board = [list(input().strip()) for i in range(r)]

if n<=1 :
    for li in board : print(''.join(li))
elif n%2==0 :
    for i in range(r): print('O'*c)
else :
    # 첫번째 폭탄이 터진 상태
    bombs1 = [['O']*c for i in range(r)]
    for y in range(r):
        for x in range(c):
            if board[y][x]=='O': bombs1[y][x] = '.'
            else :
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if y+i>=0 and y+i<r and x+j>=0 and x+j<c and board[y+i][x+j]=='O':
                        bombs1[y][x] = '.'
                        break

    # 두번째 폭탄이 터진 상태
    bombs2 = [['O']*c for i in range(r)]
    for y in range(r):
        for x in range(c):
            if bombs1[y][x]=='O' : bombs2[y][x] = '.'
            else :
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if y+i>=0 and y+i<r and x+j>=0 and x+j<c and bombs1[y+i][x+j]=='O':
                        bombs2[y][x] = '.'
                        break

    if n%4==3:
        for li in bombs1 : print(''.join(li))
    if n%4==1:
        for li in bombs2 : print(''.join(li))