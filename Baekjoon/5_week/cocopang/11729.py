import sys
k = int(sys.stdin.readline().rstrip())
array = []


def hanoi(n, start, end, mid):
    if n == 1:
        array.append([start, end])
        return
    hanoi(n-1, start, mid, end)
    array.append([start, end])
    hanoi(n-1, mid, end, start)


hanoi(k, 1, 3, 2)

print(len(array))
for i in array:
    print(i[0], i[1])
