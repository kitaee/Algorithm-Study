import sys
sys_input = sys.stdin.readline
t = int(sys_input().rstrip())
for _ in range(t):
    n = int(sys_input().rstrip())
    box = {}
    for i in range(n):
        a, b = sys_input().rstrip().split()
        if i == 0:
            box[a] = [b]
            box[b] = [a]
            print(2)
        else:
            a_get = box.get(a)
            b_get = box.get(b)
            if a_get == None and b_get == None:
                box[a] = [b]
                box[b] = [a]
                print(2)
                continue
            if a_get == None and b_get != None:
                box[a] = [b]
                box[b] = [*box[b], a]
                continue
            if b_get == None and a_get != None:
                box[b] = [a]
                box[a] = [*box[a], b]
                continue
            if b_get != None and a_get != None:
                box[b] = [*box[b], a]
                box[a] = [*box[a], b]
                continue
    print(box)