import sys


def BS(start, end, target):
    result = 0
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        for i in array:
            if i > mid:
                cnt += i-mid
        if cnt == target:
            return mid
        if cnt > target:
            start = mid + 1
            result = mid
        if cnt < target:
            end = mid - 1
    return result


n, m = map(int, sys.stdin.readline().rstrip().split())
num = 1000000000

array = list(map(int, sys.stdin.readline().rstrip().split()))

print(BS(0, num, m))
