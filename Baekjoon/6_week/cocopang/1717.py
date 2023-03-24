import sys

sys_input = sys.stdin.readline

n,m = map(int,sys_input().rstrip().split())

node = [
    i
    for i in range(n+1)
]
rank = [
    0
    for _ in range(n+1)
]
def union(x,y):
    rootX = find(x)
    rootY = find(y)
    
    if rootX == rootY:
        return
    
    if rank[rootX] < rank[rootY]:
        node[rootX] = rootY;
    else:
        node[rootY]=rootX
        if rank[rootX] == rank[rootY]:
            rank[rootX]+=1
        
    
def find(x):
    if node[x]==x:
        return x
    
    node[x] = find(node[x])
    return node[x]
    
for _ in range(m):
    c,a,b = map(int,sys_input().rstrip().split())
    if c==0:
        union(a,b)
    else:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')