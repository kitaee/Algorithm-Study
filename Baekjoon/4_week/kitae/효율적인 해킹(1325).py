import sys
input = sys.stdin.readline

from collections import deque

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
hackCount = [0 for _ in range(N+1)]

for _ in range(M):
  v1,v2 = map(int, input().split())
  graph[v2].append(v1)

for node in range(1,N+1):
  queue = deque()
  queue.append(node)
  count = 1
  visited = [False for _ in range(N+1)]
  visited[node] = True
  while queue:
    current = queue.popleft()
    if graph[current]:
      for newNode in graph[current]:
        if visited[newNode] == False:
          queue.append(newNode)
          visited[newNode] = True
          count+=1
  hackCount[node] = count

maxCount = max(hackCount)

for i in range(N+1):
  if hackCount[i] == maxCount:
    print(i, end = " ")
