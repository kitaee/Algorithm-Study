#1697번 숨바꼭질

from collections import deque

def bfs():
    q=deque()
    q.append(n)
    while q:
        v = q.popleft()
        if v==k:
            print(visited[v])
            break
        for nv in (v-1, v+1, v*2):
            if 0 <= nv <= max and visited[nv]==0:
                visited[nv]=visited[v]+1
                q.append(nv)

n,k=map(int,input().split())
max=100000
visited=[0]*(max+1)

bfs()