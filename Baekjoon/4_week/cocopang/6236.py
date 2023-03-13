import sys
sys_input = sys.stdin.readline
n,m = map(int,sys_input().rstrip().split())
array=[]

def BS(start,end,target):
    result = sys.maxsize
    while start<=end:
        mid = (start+end)//2
        sum_num = mid
        cnt = 1
        for i in array:
            if i>mid:
                cnt = target+1
                break
            if i<=sum_num:
                sum_num= sum_num-i
            else:
                cnt+=1
                sum_num= mid-i     
        if cnt > target:
            start = mid +1
        if cnt <= target:
            end = mid -1
            result = min(result,mid)
    return result
for _ in range(n):
    num = int(sys_input().rstrip())
    array.append(num)
    
print(BS(1,sum(array),m))
