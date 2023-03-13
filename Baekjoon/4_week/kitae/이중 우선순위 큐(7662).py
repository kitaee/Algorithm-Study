import sys
input = sys.stdin.readline

import heapq

T = int(input())
for _ in range(T):
  minHeap = []
  maxHeap = []
  deleteStatus = []
  count = 0
  Q = int(input())
  for _ in range(Q):
    command,num = input().split()
    if command == "I":
      heapq.heappush(minHeap, (int(num),count))
      heapq.heappush(maxHeap, (-int(num),count))
      deleteStatus.append(1)
      count+=1
    else:
      if num[0] == "-":
        while minHeap:
          if deleteStatus[minHeap[0][1]] == 1:
            deleteStatus[minHeap[0][1]] = 0
            heapq.heappop(minHeap)
            break
          heapq.heappop(minHeap)
      else:
        while maxHeap:
          if deleteStatus[maxHeap[0][1]] == 1:
            deleteStatus[maxHeap[0][1]] = 0
            heapq.heappop(maxHeap)
            break
          heapq.heappop(maxHeap)
  if sum(deleteStatus) == 0:
    print("EMPTY")
  else:
    while deleteStatus[maxHeap[0][1]] != 1:
      heapq.heappop(maxHeap)
    print(-maxHeap[0][0], end = " ")
    while deleteStatus[minHeap[0][1]] != 1:
      heapq.heappop(minHeap)
    print(minHeap[0][0])
