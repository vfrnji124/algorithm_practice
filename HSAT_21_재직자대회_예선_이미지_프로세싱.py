# 그냥 BFS만 쓰면 되는 문제인줄 알았는데, 시간초과가 나네
# 이럴 때는 어떻게 해결해야 할까?
import sys
from collections import deque
import time
start = time.time()
input = sys.stdin.readline

h, w = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(h)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def changeColor(y, x, c):
    q = deque([(y, x)])
    prevColor = image[y][x]
    image[y][x] = c
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny, nx = ey + dy[k], ex + dx[k]
            if 0<=ny<h and 0<=nx<w and image[ny][nx] == prevColor:
                image[ny][nx] = c
                q.append((ny, nx))

q = int(input())
for _ in range(q):
    y, x, c = map(int, input().split())
    changeColor(y-1, x-1, c)

for row in image:
    print(*row)
print(f'{time.time()-start:.4f} sec')