import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for _ in range(T):
    dic = {}
    queue = deque()
    F = int(input())
    for i in range(F):
        a, b = map(str, input().split())
        if a in dic:
            dic[a] += [b]
        else:
            dic[a] = [b]
        
        if b in dic:
            dic[b] += [a]
        else:
            dic[b] = [a]
        
        visited = []
        queue.append(a)
        visited.append(a)
        count = 0
        
        while queue:
            now = queue.popleft()
            count += 1
            for i in dic[now]:
                if not i in visited:
                    queue.append(i)
                    visited.append(i)
                    
        print(count)
