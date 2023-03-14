import sys
from collections import deque
sys_input = sys.stdin.readline

t = int(sys_input().rstrip())


def bfs(a, target):
    box = deque([])
    box.appendleft([a, ''])
    while len(box):
        v = box.popleft()
        if v[0] > 9999:
            continue
        if visited[v[0]]:
            continue
        visited[v[0]] = True
        if v[0] == target:
            print(v[1])
            return
        if v[0]*2 > 9999:
            box.append([v[0]*2 % 10000, v[1]+'D'])
        else:
            box.append([v[0]*2, v[1]+'D'])

        if v[0] == 0:
            box.append([9999, v[1]+'S'])
        else:
            box.append([v[0]-1, v[1]+'S'])

        if v[0] < 10:
            RL_num = v[0]*10
            RR_num = v[0]*1000
        elif v[0] < 100:
            RL_num = v[0]*10
            mod_num = v[0] % 10
            div_num = v[0]//10
            RR_num = 1000*mod_num + div_num
        elif v[0] < 1000:
            RL_num = v[0]*10
            mod_num = v[0] % 10
            sub_num = v[0]-mod_num
            div_num = sub_num//10
            RR_num = 1000 * mod_num + div_num
        else:
            mod_num = v[0] % 1000
            sub_num = v[0] - mod_num
            div_num = sub_num//1000
            RL_num = mod_num*10 + div_num
            mod_num = v[0] % 10
            div_num = v[0]//10
            RR_num = 1000*mod_num + div_num
        box.append([RL_num, v[1]+'L'])
        box.append([RR_num, v[1]+'R'])


for _ in range(t):
    a, b = map(int, (sys_input().rstrip().split()))
    visited = [False]*(10001)
    bfs(a, b)
