from collections import deque

n, k = map(int, input().split())
dist = [0 for _ in range(100001)]

queue = deque()
queue.append(n)

while queue:
  value = queue.popleft()
  if value == k:
    print(dist[value])
  else:
    if 0 <= value-1 <= 100000 and dist[value-1] == 0:
      dist[value-1] = dist[value]+1
      queue.append(value-1)
    if 0 <= value+1 <= 100000 and dist[value+1] == 0:
      dist[value+1] = dist[value]+1
      queue.append(value+1)
    if 0 <= value*2 <= 100000 and dist[value*2] == 0:
      dist[value*2] = dist[value]+1
      queue.append(value*2)
