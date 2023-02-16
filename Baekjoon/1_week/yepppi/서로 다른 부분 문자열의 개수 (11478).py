S = input().strip()

result = set()

for i in range(len(S)):
  for j in range(len(S)-i):
    result.add(S[j:j+i+1])
    
print(len(result))
