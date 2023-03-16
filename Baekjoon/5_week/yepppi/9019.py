import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for _ in range(T):
  a, b = map(int, input().rstrip().split())
  queue = deque()
  queue.append((a, ''))
  visited = [False] * 10001
  visited[a] = True
  
  while queue:
    num, result = queue.popleft()
    
    if num == b:
      print(result)
      break
  
    temp = (num*2)%10000
    if visited[temp] == False:
      queue.append((temp, result+'D'))
      visited[temp] = True
  
    temp = (num-1)%10000
    if visited[temp] == False:
      queue.append((temp, result+'S'))
      visited[temp] = True
  
    temp = (num%1000)*10+num//1000
    if visited[temp] == False:
      queue.append((temp, result+'L'))
      visited[temp] = True
  
    temp = (num%10)*1000+num//10
    if visited[temp] == False:
      queue.append((temp, result+'R'))
      visited[temp] = True
