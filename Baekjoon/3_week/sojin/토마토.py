from collections import deque


m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    while q:
        x, y = q.popleft()
        for nx, ny in ((x-1,y),(x,y-1),(x+1,y),(x,y+1)):
             if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                  box[nx][ny] = box[x][y] + 1
                  q.append((nx,ny))

q = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i,j))


bfs()

result = 0

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        result = max(result, box[i][j])

if result == 1:
    print(0)

else:
    print(result - 1)