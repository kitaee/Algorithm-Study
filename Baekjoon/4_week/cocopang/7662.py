import sys
import heapq
sys_input = sys.stdin.readline
t = int(sys_input().rstrip())


def heap_delete(heap):
    while heap and is_delete[heap[0][1]]:
        heapq.heappop(heap)


for _ in range(t):
    k = int(sys_input().rstrip())
    max_heap = []
    min_heap = []
    is_delete = []
    check = 0
    for _ in range(k):
        s, n = sys_input().rstrip().split()
        n = int(n)
        if s == 'I':
            heapq.heappush(max_heap, (-n, check))
            heapq.heappush(min_heap, (n, check))
            check += 1
            is_delete.append(False)
        if s == 'D':
            if n == 1 and len(max_heap):
                v = heapq.heappop(max_heap)
                is_delete[v[1]] = True
            if n == -1 and len(min_heap):
                v = heapq.heappop(min_heap)
                is_delete[v[1]] = True
        heap_delete(max_heap)
        heap_delete(min_heap)
    if len(max_heap) and len(min_heap):
        print(-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0])
    else:
        print('EMPTY')
