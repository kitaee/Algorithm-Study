from collections import deque

a, b = map(int, input().split())
queue = deque([(a, 1)])
answer = -1

while queue:
  now, minimum = queue.popleft()

  if now == b:
    answer = minimum
    break

  if now*2 <= b:
    queue.append((now*2, minimum+1))
  
  if int(str(now)+'1') <= b:
    queue.append((int(str(now)+'1'), minimum+1))

print(answer)
