import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  card = []
  n = int(input())
  for _ in range(2):
    card.append(list(map(int, input().split())))
  dp = [[0 for _ in range(n)] for _ in range(2)]

  if n ==1:
    print(max(card[0][0], card[1][0]))
    continue

  dp[0][0],dp[1][0] = card[0][0],card[1][0]
  dp[0][1] = card[0][1] + dp[1][0]
  dp[1][1] = card[1][1] + dp[0][0]

  for i in range(2,n):
    dp[0][i] = max(card[0][i]+dp[1][i-1], card[0][i]+dp[1][i-2])
    dp[1][i] = max(card[1][i]+dp[0][i-1], card[1][i]+dp[0][i-2])

  print(max(dp[0][-1], dp[1][-1]))
