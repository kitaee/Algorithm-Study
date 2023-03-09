import sys
from collections import deque
sys_input = sys.stdin.readline


def bfs(c_x, c_y, cnt):
    box.appendleft([c_x, c_y, cnt])
    while len(box):
        v = box.popleft()
        visited[v[0]][v[1]] = True
        if v[0] == l_x and v[1] == l_y:
            print(v[2])
            break
        for x, y in zip(dx, dy):
            nx = x + v[0]
            ny = y + v[1]
            ncnt = v[2]
            if in_range(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            box.append([nx, ny, ncnt+1])


t = int(sys_input().rstrip())
dx = [-2, 2, -2, 2, -1, 1, 1, -1]
dy = [-1, 1, 1, -1, -2, 2, -2, 2]


def in_range(nx, ny):
    return nx < 0 or nx >= l or ny < 0 or ny >= l


for _ in range(t):
    global l
    l = int(sys_input().rstrip())
    box = deque([])
    cnt = 0
    visited = [
        [False]*l
        for _ in range(l)
    ]
    c_x, c_y = map(int, sys_input().rstrip().split())
    l_x, l_y = map(int, sys_input().rstrip().split())
    bfs(c_x, c_y, cnt)
