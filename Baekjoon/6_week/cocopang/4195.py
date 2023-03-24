import sys

sys_input = sys.stdin.readline

t = int(sys_input().rstrip())


def node_check(target):
    global index
    if friend.get(target) == None:
        node.append(index)
        rank.append(0)
        friend[target] = index
        visited.append(1)
        index += 1


def find(x):
    if node[x] == x:
        return x
    node[x] = find(node[x])
    return node[x]


def union(a, b, x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX == rootY:
        return visited[rootX]
    result = visited[rootX]+visited[rootY]
    if rank[rootX] < rank[rootY]:
        node[rootX] = rootY
        friend[a] = rootY
    else:
        node[rootY] = rootX
        friend[b] = rootX
        if rank[rootX] == rank[rootY]:
            rank[rootX] += 1
    visited[rootX] = result
    visited[rootY] = result
    return result


for _ in range(t):
    global rootX, rootY
    n = int(sys_input().rstrip())
    node = []
    friend = {}
    rank = []
    visited = []
    index = 0
    for _ in range(n):
        check = 0
        a, b = sys_input().rstrip().split()
        node_check(a)
        node_check(b)
        print(union(a, b, friend[a], friend[b]))
