import sys
from collections import deque
box = deque([])
a, b = map(int, sys.stdin.readline().rstrip().split())


def bfs(a, b):

    box.appendleft([a, 0])
    check = False
    while len(box):
        v = box.popleft()
        if v[0] > b:
            continue
        if v[0] == b:
            print(v[1]+1)
            check = True
            break
        box.append([(v[0]*2), v[1]+1])
        box.append([(v[0]*10)+1, v[1]+1])
    if not check:
        print(-1)


bfs(a, b)
