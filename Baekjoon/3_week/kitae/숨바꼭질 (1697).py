import sys
input = sys.stdin.readline

from collections import deque

N,K = map(int, input().split())
MAX = 200000
visited = [False for _ in range(MAX)]
visited[N] = True
queue = deque()
queue.append((N,0))

while queue:
  current, time = queue.popleft()
  if current == K:
    print(time)
    break
  for newPosition in [current-1, current+1, current*2]:
    if 0 <= newPosition < MAX and visited[newPosition] == False:
      queue.append((newPosition, time+1))
      visited[newPosition] = True
