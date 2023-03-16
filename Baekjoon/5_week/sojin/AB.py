import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque([(a, 1)])
    while q:
        v, cnt = q.popleft()
        if v == b :
            return cnt
        for nv in (v*2, v*10+1):
            if 1<=nv<=10**9 :
                q.append((nv,cnt+1))


a, b = map(int, input().split())
result = bfs()
if result is None:
    print(-1)
else:
    print(result)