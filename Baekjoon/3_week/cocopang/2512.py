import sys

n = int(sys.stdin.readline().rstrip())

array = list(map(int, sys.stdin.readline().rstrip().split()))
max_m = max(array)

m = int(sys.stdin.readline().rstrip())


def BS(start, end, target):
    result = 0
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        for i in array:
            if i-mid < 0:
                cnt += i
            else:
                cnt += mid
        if cnt == target:
            return mid
        if cnt > target:
            end = mid - 1
        if cnt < target:
            start = mid + 1
            result = mid
    return result


print(BS(1, max_m, m))
