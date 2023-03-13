import sys
input = sys.stdin.readline

from collections import deque

def convertNum(A,B):
  queue = deque()
  queue.append((A,1))
  
  while queue:
    num, count = queue.popleft()
    if num == B:
      return count
    elif num > B:
      continue
    queue.append((num*2, count+1))
    queue.append((int(str(num)+'1'), count+1))
  return -1

A,B = map(int, input().split())
print(convertNum(A,B))
