#2805번 나무자르기

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)
while start <= end:
    total = 0
    mid = (start+end)//2

    for tree in trees:
        if tree > mid:
            total += tree - mid
        if total > m:
            break

    if total >= m:
        start = mid + 1
        
    else:
        end = mid - 1

print(end)