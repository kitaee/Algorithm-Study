S = input()
stringSet = set()
stringLength = len(S)
answer = 0

for i in range(stringLength):
  for j in range(1,stringLength+1):
    if i+j > stringLength:
      break
    stringSet.add(S[i:i+j])

print(len(stringSet))
