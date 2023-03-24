import sys
sys_input = sys.stdin.readline

n = int(sys_input().rstrip())
array = []
for i in range(n):
    x,y = map(int,sys_input().rstrip().split())
    array.append([x,y])
array.sort(key = lambda x: (x[1],x[0]))
cnt = 0
for idx,val in enumerate(array):
    if idx==0:
        cx,cy = val
        cnt+=1
        continue
    if val[0]==val[1]:
        cnt+=1
        continue
    if cy<=val[0]:
        cx,cy = val
        cnt+=1
        continue
print(cnt)