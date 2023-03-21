from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(graph, visited, N, y, x):
  queue = deque()
  queue.append((y,x))
  visited[y][x] = True
  count = 1
  while queue:
    yIndex, xIndex = queue.popleft()
    for i in range(4):
      ny = yIndex + dy[i]
      nx = xIndex + dx[i]
      if 0<=ny<N and 0<=nx<N and graph[ny][nx] == '1' and visited[ny][nx] == False:
        visited[ny][nx] = True
        queue.append((ny,nx))
        count+=1
  return count

N = int(input())
visited = [[False for _ in range(N)] for _ in range(N)]
totalCount = []
graph = []
for _ in range(N):
  tempGraph = list(input())
  graph.append(tempGraph)

for y in range(N):
  for x in range(N):
    if graph[y][x] == '1' and visited[y][x] == False:
      totalCount.append(bfs(graph,visited,N,y,x))
totalCount.sort()
print(len(totalCount))
for count in totalCount:
  print(count)
