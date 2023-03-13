#7562번 나이트의 이동

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

def bfs():
    q = deque()
    q.append((sx, sy))
    while q :
        x, y = q.popleft()
        if x == ex and y == ey :
            return chess[x][y] -1
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<l and 0<=ny<l and chess[nx][ny]==0:
                chess[nx][ny] = chess[x][y] + 1
                q.append((nx,ny))

t= int(input())
for _ in range(t) :
    l = int(input())
    chess = [[0]*l for _ in range(l)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    chess[sx][sy]=1
    print(bfs())
