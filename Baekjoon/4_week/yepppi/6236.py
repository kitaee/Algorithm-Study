n, m = map(int, input().split())
money = []

for _ in range(n):
    money.append(int(input().rstrip()))
    
start, end = min(money), sum(money)
answer = sum(money)
    
while start <= end:
    mid = (start + end) // 2
    
    times = 1
    count = 0
    is_small = False
    
    for budget in money:
        
        if budget > mid:
            is_small = True
            break
        
        if count + budget > mid:
            times += 1
            count = budget
        else:
            count += budget
    
    if is_small == True:
        start = mid + 1
    else:
        if times > m:
            start = mid + 1
        else:
            end = mid - 1
            answer = min(answer, mid)

print(answer)
