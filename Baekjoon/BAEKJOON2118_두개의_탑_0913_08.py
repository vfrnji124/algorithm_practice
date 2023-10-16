# 백준 2118: 두 개의 탑-(누적합, 투포인터)
# 각 지점들은 차례로, 원형으로 연결
# 지점들 중 두곳에 탑을 세우려고 한다.
# 두 탑의 거리가 최대가 되록 하고자 한다.
# 지점들이 원형으로 연결되어 있기 때문에, 시계방향과 반시계방향 두경로가 존재.
# 두 지점 사이 거리는 둘 중 더 작은 값을 거리로 한다.
# 두 지점 사이의 거리가 주어졌을 때 최댓값을 계산하는 프로그램을 작성

import sys
input = sys.stdin.readline

n = int(input())
dists = [int(input()) for _ in range(n)]

ps = [0] * (2 * n + 1)
for i in range(2 * n):
    ps[i + 1] = ps[i] + dists[i % n]

ans = 0
total, right = sum(dists), 1
for left in range(2 * n):
    while right < 2 * n + 1 and ps[right] - ps[left] <= total - ps[right] + ps[left]:
        ans = max(ans, ps[right] - ps[left])
        right += 1
print(ans)