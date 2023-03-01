import sys
input = sys.stdin.readline

N = int(input())
cost = []

for _ in range(N):
  cost.append(list(map(int, input().split())))

for i in range(1,N):
  cost[i][0] += min(cost[i-1][1], cost[i-1][2])
  cost[i][1] += min(cost[i-1][0], cost[i-1][2])
  cost[i][2] += min(cost[i-1][0], cost[i-1][1])

print(min(cost[-1]))
