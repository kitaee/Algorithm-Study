import sys
from collections import deque
n,m = map(int,sys.stdin.readline().rstrip().split())

array = [
    list(map(int,sys.stdin.readline().rstrip().split()))
    for _ in range(m)
]
dx,dy=[-1,1,0,0],[0,0,-1,1]
box = deque([])
def in_ragne(nx,ny):
    return nx < 0 or nx >=m or ny<0 or ny>=n
def bfs():
    for i in range(m):
        for j in range(n):
            if array[i][j] == 1:
                box.append([i,j,0])
    while len(box):
        global vd
        vx,vy,vd = box.popleft()
        for x,y in zip(dx,dy):
            nx,ny = x+vx,y+vy
            if in_ragne(nx,ny):
                continue
            if array[nx][ny] !=0:
                continue
            array[nx][ny]=1
            box.append([nx,ny,vd+1])
            
        

bfs()
check = True
for i in range(m):
    if not check:
        break
    for j in range(n):
        if array[i][j]==0:
            check = False
if check:
    print(vd)
else:
    print(-1)