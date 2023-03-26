import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
array = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
check = []

def dfs(x, y):
  array[x][y] = '0'
  check[-1] += 1
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<n and 0<=ny<n:
      if array[nx][ny] == '1':
        dfs(nx, ny)

count = 0
for i in range(n):
  for j in range(n):
    if array[i][j] == '1':
      count += 1
      check.append(0)
      dfs(i, j)

print(count)
check.sort()
print(*check, sep = "\n")
