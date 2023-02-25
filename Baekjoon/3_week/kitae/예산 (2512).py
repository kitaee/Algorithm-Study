import sys
input = sys.stdin.readline

def calculate(moneyRequest, money, M):
  sum = 0
  for request in moneyRequest:
    if request <= money:
      sum += request
    else:
      sum += money
      
    if sum > M:
      break
  return sum

answer = 0
N = int(input())
moneyRequest = list(map(int, input().split()))
M = int(input())

start, end = 0, max(moneyRequest)

while start <= end:
  mid = (start+end) // 2
  tempMoney = calculate(moneyRequest, mid, M)
  if tempMoney <= M:
    start = mid + 1
    answer = mid
  else:
    end = mid - 1

print(answer)
