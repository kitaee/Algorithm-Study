import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int,input().rstrip().split())

    visited = [False]*10001
    q = deque([(a,'')])
    visited[a] = True

    while q:
        num, op = q.popleft()

        if num == b:
            print(op)
            break

        d = num * 2 % 10000
        if not visited[d]:
            visited[d] = True
            q.append((d, op + 'D'))

        s = (num-1) % 10000
        if not visited[s]:
            visited[s] = True
            q.append((s, op + 'S'))

        l = num // 1000 + (num % 1000)*10
        if not visited[l]:
            visited[l] = True
            q.append((l, op + 'L'))

        r = num // 10 + (num % 10)*1000
        if not visited[r]:
            visited[r] = True
            q.append((r, op + 'R'))

    

