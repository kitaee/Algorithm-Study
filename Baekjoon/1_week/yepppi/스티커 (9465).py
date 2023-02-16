import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())
result = []

for _ in range(T):
  n = int(input())
  array = [list(map(int, input().split())) for _ in range(2)]

  if n == 1:
    print(max(array[0][0], array[1][0]))
    continue
  
  dp = [[0]*n for _ in range(2)]
  dp[0][0] = array[0][0]
  dp[1][0] = array[1][0]
  dp[0][1] = array[1][0] + array[0][1]
  dp[1][1] = array[0][0] + array[1][1]
  
  for i in range(2, n):
    dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + array[0][i]
    dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + array[1][i]

  result.append(max(dp[0][-1], dp[1][-1]))

print(*result, sep = "\n")
