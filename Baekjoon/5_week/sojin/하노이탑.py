def hanoi(n, start, end):
    tmp = 6 - start - end
    if n == 1:
        print(start, end)
        return
    
    hanoi(n-1, start, tmp)
    print(start, end)
    hanoi(n-1, tmp, end)

n = int(input())
print(2**n - 1)
hanoi(n,1,3)
