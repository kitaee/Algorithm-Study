import sys
from collections import deque
n, k = map(int, sys.stdin.readline().rstrip().split())
box = deque([])
max_num = 200001
visited = [False]*max_num
result = [0]*max_num


def bfs(n):
    box.appendleft(n)
    while len(box):
        v = box.popleft()
        if v == k:
            print(result[v])
            break
        if v*2 >= max_num or v < 0:
            continue
        if not visited[v-1]:
            box.append(v-1)
            visited[v-1] = True
            result[v-1] = result[v]+1
        if not visited[v+1]:
            box.append(v+1)
            visited[v+1] = True
            result[v+1] = result[v]+1
        if not visited[v*2]:
            box.append(v*2)
            visited[v*2] = True
            result[v*2] = result[v]+1


bfs(n)
