s='ababc'

spart =[]
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        spart.append(s[i:j])

result = []
for a in spart:
    if a not in result:
        result.append(a)

answer = len(result)
print(answer)


