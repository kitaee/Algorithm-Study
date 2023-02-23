import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree)
  
while start <= end:
  mid = (start+end)//2

  count = 0
  for i in tree:
    if i >= mid:
      count += (i-mid)

  if count >= m:
    start = mid+1
  else:
    end = mid-1

print(end)
