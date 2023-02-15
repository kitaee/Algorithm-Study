s = input()

result = set()
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        result.add(s[i:j])

print(len(result))
