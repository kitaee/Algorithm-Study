import sys
input = sys.stdin.readline

from collections import deque

T = int(input().rstrip())

for _ in range(T):
    I = int(input().rstrip())
    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())
    
    dx = [-1, -1, 1, 1, -2, -2, 2, 2]
    dy = [-2, 2, -2, 2, -1, 1, -1, 1]
    
    visited = [[False for _ in range(I)] for _ in range(I)]
    
    queue = deque()
    queue.append((startX, startY, 0))
    
    while queue:
        x, y, count = queue.popleft()
        visited[x][y] = True
        
        if x == endX and y == endY:
            print(count)
            continue
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<I and 0<=ny<I and visited[nx][ny] == False:
                queue.append((nx, ny, count+1))
                visited[nx][ny] = True
