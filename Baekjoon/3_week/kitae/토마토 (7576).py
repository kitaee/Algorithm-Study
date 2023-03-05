import sys
input = sys.stdin.readline

from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def getTomatoIndex(tomato, N, M):
  queue = deque()
  for i in range(M):
    for j in range(N):
      if tomato[i][j] == 1:
        queue.append((i,j))
  return queue

def bfs(tomato, visited, tomatoList, N, M):
  while tomatoList:
    yIndex, xIndex = tomatoList.popleft()
    visited[yIndex][xIndex] = True
    for i in range(4):
      nx = xIndex + dx[i]
      ny = yIndex + dy[i]

      if 0 <= nx < N and 0 <= ny < M and visited[ny][nx] == False and tomato[ny][nx] == 0:
        tomato[ny][nx] = tomato[yIndex][xIndex] + 1
        tomatoList.append((ny,nx))

def isPossible(tomato):
  for tempTomato in tomato:
    if 0 in tempTomato:
      return False
  return True

def getMaximumDay(tomato):
  answer = -1
  for tempTomato in tomato:
    maximumDay = max(tempTomato)
    if answer < maximumDay:
      answer = maximumDay
  return answer


N,M = map(int, input().split())
tomato = []
for _ in range(M):
  tomato.append(list(map(int, input().split())))

tomatoList = getTomatoIndex(tomato, N, M)
visited = [[False for _ in range(N)] for _ in range(M)]

bfs(tomato, visited, tomatoList, N, M)

if isPossible(tomato):
  print(getMaximumDay(tomato)-1)
else:
  print(-1)
