import sys
input = sys.stdin.readline

from collections import deque

dy = [-2,-2,-1,-1,1,1,2,2]
dx = [1,-1,2,-2,2,-2,1,-1]

def bfs(visited, current_x, current_y, target_x, target_y, I):
  queue = deque()
  queue.append((current_y,current_x,0))
  visited[current_y][current_x] = True

  while queue:
    yIndex, xIndex, count = queue.popleft()
    if yIndex == target_y and xIndex == target_x:
      return count
    for i in range(8):
      ny = yIndex + dy[i]
      nx = xIndex + dx[i]
      if 0<=nx<I and 0<=ny<I and visited[ny][nx] == False:
        queue.append((ny,nx,count+1))
        visited[ny][nx] = True

T = int(input())
for _ in range(T):
  I = int(input())
  current_x, current_y = map(int, input().split())
  target_x, target_y = map(int, input().split())
  visited = [[False for _ in range(I)] for _ in range(I)]
  print(bfs(visited,current_x,current_y,target_x,target_y,I))
