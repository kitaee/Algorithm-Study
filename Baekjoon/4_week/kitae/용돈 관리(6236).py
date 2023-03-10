import sys
input = sys.stdin.readline
MAX = sys.maxsize

def spendMoney(moneyList, budget, M):
  count = 1
  totalBudget = budget
  for money in moneyList:
    if budget < money:
      return M+1
    elif totalBudget < money:
      count+=1
      totalBudget = budget
      totalBudget -= money
    else:
      totalBudget -= money
  return count
      
moneyList = []
answer = MAX
N,M = map(int, input().split())
for _ in range(N):
  moneyList.append(int(input()))

start, end = min(moneyList), sum(moneyList)

while start <= end:
  mid = (start+end) // 2
  count = spendMoney(moneyList, mid, M)
  if count > M:
    start = mid + 1
  else:
    end = mid - 1
    if mid < answer:
      answer = mid

print(answer)
