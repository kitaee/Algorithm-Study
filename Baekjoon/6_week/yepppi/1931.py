n = int(input())
meeting = []
for _ in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))
    
meeting.sort(key=lambda x: (x[1], x[0]))

answer = 0
count = 0
for s, e in meeting:
    if s >= count:
        answer += 1
        count = e
        
print(answer)
