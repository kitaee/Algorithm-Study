import sys
from collections import deque

sys_input = sys.stdin.readline

box = deque([])
apart = []
n = int(sys_input().rstrip())

array = [
    list(map(int,sys_input().rstrip()))
    for _ in range(n)
]
visited =[
    [False]*n
    for _ in range(n)
]
dx,dy = [-1,1,0,0],[0,0,-1,1]
cnt_apart = 0
def in_range(nx,ny):
    return nx<0 or nx>=n or ny<0 or ny>=n
def bfs(i,j):
    box.appendleft([i,j])
    visited[i][j]=True
    array[i][j]=0
    cnt = 1
    while len(box):
        v = box.popleft()
        for x,y in zip(dx,dy):
            nx = v[0] + x
            ny = v[1] + y
            if in_range(nx,ny):
                continue
            if array[nx][ny]==0:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny]==True
            array[nx][ny]=0
            cnt+=1
            box.append([nx,ny])
    apart.append(cnt)
  
for i in range(n):
    for j in range(n):
        if int(array[i][j])==1:
            bfs(i,j)
            cnt_apart+=1

print(cnt_apart)
apart.sort()
for i in apart:
    print(i)