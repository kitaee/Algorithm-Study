import sys
input = sys.stdin.readline

def hanoi(n, start, dest) :
    if n == 1:
        print(start, dest)
        return
    hanoi(n-1, start, 6-start-dest)
    print(start, dest)
    hanoi(n-1, 6-start-dest, dest)
    
N = int(input())
print(2**N-1)
hanoi(N, 1, 3)
