import sys
from pprint import pprint
input = sys.stdin.readline

h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]

# print('input----->')
# pprint(grid)
# print('<-----input')

d_mark = ['^', '>', 'v', '<']
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def findStart(grid):
    # print('findStart----->')
    for j in range(h):
        for i in range(w):
            if grid[j][i] == '#':
                direction = findDirection(j, i)
                # print(f'direction: {direction}')
                if direction != -1:
                    # print(f'start (y, x): ({j}, {i})')
                    print(j+1, i+1)
                    # print(f'direction: {d_mark[direction]}')
                    print(d_mark[direction])
                    # print('<-----findStart')
                    return j, i, direction

def findDirection(y, x):
    # print('findDirection----->')
    count = 0
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < h and 0 <= nx < w:
            if grid[ny][nx] == '#':
                # print(f'ny, nx: ({ny}, {nx})')
                direction = k
                count += 1
                # print(f'direction, count : {direction}, {count}')
    # print('<-----findDirection')
    return direction if count == 1 else -1

def navigate(y, x, direction):
    grid[y][x] = '.'
    prevDir = nextDir = direction
    while True:
        while prevDir == nextDir:
            print('A', end='')
            y = y + dy[prevDir]
            x = x + dx[prevDir]
            grid[y][x] = '.'
            y = y + dy[prevDir]
            x = x + dx[prevDir]
            grid[y][x] = '.'

            nextDir = findDirection(y, x)
            # print(f'prevDir, nextDir : {prevDir}, {nextDir}')
        if nextDir == -1:
            return
        if (nextDir - prevDir) % 4 == 1:
            print('R', end='')
        elif (nextDir - prevDir) % 4 == 3:
            print('L', end='')
        prevDir = nextDir

sy, sx, direction = findStart(grid)
navigate(sy, sx, direction)