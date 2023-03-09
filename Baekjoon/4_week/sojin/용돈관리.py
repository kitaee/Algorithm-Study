#

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]

start = min(money)
end = sum(money)

while start <= end:
    mid = (start + end) // 2
    now = mid
    num = 1
    for i in range(n):
        if now < money[i]:
            now = mid
            num += 1
        now -= money[i]

    if num > m or mid < max(money):
        start = mid + 1
    else:
        end = mid - 1
        k = mid

print(k)