import sys
from collections import deque
sys_input = sys.stdin.readline

n,m = map(int,sys_input().rstrip().split())

graph = [
    []
    for _ in range(n+1)
]
box = deque([])
max_num = -sys.maxsize
result = []
for _ in range(m):
    f,s = map(int,sys_input().rstrip().split())
    graph[s].append(f)
for i in range(1,n+1):
    cnt = 0
    box.appendleft(graph[i])
    visited = [False]*(n+1)
    visited[i]=True
    while len(box):
        v = box.popleft()
        for j in v:
            if not visited[j]:
                box.append(graph[j])
                cnt+=1
                visited[j]=True
    max_num = max(max_num,cnt)
    result.append(cnt)

for z in range(n):
    if max_num==result[z]:
        print(z+1,end=" ")
