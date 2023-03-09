#7662번 이중 우선순위 큐

import sys
import heapq
input = sys.stdin.readline

def sync(arr):
    while arr and visited[arr[0][1]] == 0:
        heapq.heappop(arr)

for _ in range(int(input())):
    min_heap, max_heap = [], []
    visited = [0] * 1000000

    k = int(input())
    for i in range(k):
        op, num = input().split()
        num = int(num)

        if op == "I":
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = 1
            
        else:
            if num == 1:
                sync(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)

            elif num == -1:
                sync(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)

sync(max_heap)
sync(min_heap)

if min_heap and max_heap:
    print(-max_heap[0][0], min_heap[0][0])

else:
    print('EMPTY')