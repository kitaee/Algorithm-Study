#1325번 효율적인 해킹

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())

def bfs(v):
    cnt = 1
    queue = deque()
    queue.append(v)
    visited = [0]*(n+1)
    visited[v] = 1
    while queue:
        x = queue.popleft()
        for nx in com[x]:
            if visited[nx] == 0:
                visited[nx] = 1
                cnt += 1
                queue.append(nx)
    return cnt

com = [[] for _  in range(n+1)]

for _ in range(m):
    t, td = map(int, input().split())
    com[td].append(t)

max_cnt = 0
results = []

for i in range(1,n+1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
        results.clear()
        results.append(i)
    elif cnt == max_cnt:
        results.append(i)

print(*results)