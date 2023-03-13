import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    end, start = map(int, input().split())
    graph[start].append(end)

queue = deque()

def bfs(num):
    visited = [False for _ in range(n+1)]
    visited[num] = True
    
    count = 1
    queue.append(num)
    
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visited[next] == False:
                visited[next] = True
                queue.append(next)
                count += 1
    return count

result = [0 for _ in range(n+1)]
for i in range(1, n+1):
    result[i] = bfs(i)
    
answer = max(result)
for i in range(len(result)):
    if result[i] == answer:
        print(i, end=' ')
