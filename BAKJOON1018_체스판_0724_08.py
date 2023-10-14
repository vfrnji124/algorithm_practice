# 백준 1018: 체스판 다시 칠하기(아이디어가 안떠오르는데??)

# 문제 요약
# M*N 크기의 보드가 주어진다. 이를 잘라서 8*8 크기의 체스판으로 제작
# 맨왼쪽 위칸이 흰색, 또는 검은색인 두가지 경우만 존재
# 주어진 체스판 어디에서 자르든 상관없이 8*8크기의 체스판을 만들 수 있고, 이때 새로 칠해야 하는 정사각형의 최소 개수를 구하라

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chess_table = [list(input().strip()) for _ in range(N)]
answer = sys.maxsize

for j in range(N - 7):
    for i in range(M - 7):
        topleft_W = 0
        topleft_B = 0
        for c in range(j, j + 8):
            for r in range(i, i + 8):
                if (c + r) % 2 == 0:
                    if chess_table[c][r] != 'W':
                        topleft_W += 1
                    else:
                        topleft_B += 1
                else:
                    if chess_table[c][r] != 'B':
                        topleft_W += 1
                    else:
                        topleft_B += 1
        answer = min(topleft_W, topleft_B, answer)
        
print(answer)