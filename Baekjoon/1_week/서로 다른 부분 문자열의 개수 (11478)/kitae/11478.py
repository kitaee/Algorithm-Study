S = input()
stringSet = set()

for i in range(len(S)):
  for j in range(1,len(S)+1):
    if i+j > len(S):
      break
    stringSet.add(S[i:i+j])

print(len(stringSet))
