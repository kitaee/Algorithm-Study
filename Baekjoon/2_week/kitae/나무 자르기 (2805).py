import sys
input = sys.stdin.readline

def cutTree(trees, height):
  sum = 0
  for tree in trees:
    if tree <= height:
      continue
    sum += (tree-height)
  return sum

answer = 0
N,M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
start = 0
end = trees[-1]

while start <= end:
  mid = (start + end) // 2
  if cutTree(trees, mid) >= M:
    answer = mid
    start = mid + 1
  else:
    end = mid - 1

print(answer)
