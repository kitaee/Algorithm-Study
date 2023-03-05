n = int(input().rstrip())
requests = list(map(int, input().split()))
m = int(input().rstrip())

if sum(requests) <= m:
  print(max(requests))
else:
  start, end = 1, max(requests)
  answer = 0
  while start <= end:
    mid = (start + end) // 2

    count = 0
    for budget in requests:
      if mid >= budget:
        count += budget
      else:
        count += mid
        
    if count > m:
      end = mid - 1
    elif count == m:
      answer = mid
      break
    else:
      start = mid + 1
      answer = mid
      
  print(answer)
