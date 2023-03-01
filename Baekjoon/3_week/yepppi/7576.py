from collections import deque

m, n = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(n)]
day = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

for i in range(n):
  for j in range(m):
    if tomatoes[i][j] == 1:
      queue.append([i, j])

while queue:
  x, y = queue.popleft()
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<n and 0<=ny<m and tomatoes[nx][ny] == 0:
      tomatoes[nx][ny] = tomatoes[x][y] + 1
      queue.append([nx, ny])

if any(0 in i for i in tomatoes):
  print(-1)
else:
  print(max(map(max, tomatoes))-1)
