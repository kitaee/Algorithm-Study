import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = []
for i in range(n+1):
    parent.append(i)

def find_parent(num):
    if parent[num] == num:
        return num
    temp = find_parent(parent[num])
    parent[num] = temp
    return parent[num]
    
def union_find(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        return
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_find(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')
