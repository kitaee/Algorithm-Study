def hanoi(n, start, end):
    temp = 6-start-end
    
    if n==1:
        print(start, end)
        return
    
    hanoi(n-1, start, temp)
    print(start, end)
    hanoi(n-1, temp, end)
    
n = int(input())
print(2**n-1)
hanoi(n, 1, 3)
