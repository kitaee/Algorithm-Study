#2512번 예산

N = int(input())
cts = list(map(int, input().split()))
M = int(input())

start , end = 0, max(cts)

if M >= sum(cts):
    print(max(cts))

else :
    while start <= end:
        mid = (start+end) // 2
        total = 0
        
        for ct in cts:
            total += min(ct, mid)
            if total > M:
                break

        if total > M :
            end = mid - 1
        else :
            start = mid + 1

    print(end)