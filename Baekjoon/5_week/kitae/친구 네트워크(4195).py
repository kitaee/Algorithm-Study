import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def findParent(parent, node):
  if parent[node] != node:
    parent[node] = findParent(parent, parent[node])
  return parent[node]

def unionParent(parent, node1, node2, parentCount):
  node1 = findParent(parent, node1)
  node2 = findParent(parent, node2)
  if node1 < node2:
    parentCount[node1] += parentCount[node2]
    parent[node2] = node1
  else:
    parentCount[node2] += parentCount[node1]
    parent[node1] = node2
    
T = int(input())
for _ in range(T):
  parent = []
  parentCount = []
  nameDict = dict()
  nameIndex = 0
  F = int(input())
  for _ in range(F):
    name1, name2 = input().split()
    if name1 not in nameDict:
      nameDict[name1] = nameIndex
      parent.append(nameIndex)
      parentCount.append(1)
      nameIndex+=1
    if name2 not in nameDict:
      nameDict[name2] = nameIndex
      parent.append(nameIndex)
      parentCount.append(1)
      nameIndex+=1
    unionParent(parent, nameDict[name1], nameDict[name2], parentCount)
    print(parentCount[0])
