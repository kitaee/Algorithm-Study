from collections import deque

N = int(input())
visited = [[False for _ in range(N)] for _ in range(N)]
result = []

array = []
for _ in range(N):
    array.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

def bfs(x, y):
    queue.append((x, y))
    visited[x][y] = True
    num = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and array[nx][ny] == '1' and visited[nx][ny] == False:
                visited[nx][ny] = True
                num += 1
                queue.append((nx, ny))
    result.append(num)
            
            
count = 0
for i in range(N):
    for j in range(N):
        if array[i][j] == '1' and visited[i][j] == False:
            count += 1
            bfs(i, j)
print(count)
result.sort()
print(*result, sep='\n')
