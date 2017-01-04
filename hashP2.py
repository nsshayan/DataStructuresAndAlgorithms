'''
Given an input string. Print the character that has repeated maximum number of times.

aaaAAA
A 3
AAA!!!!!
! 5
'''
inputString = raw_input()

inputDic = {}

for i in range(len(inputString)):
    if inputDic.has_key(inputString[i]):
        inputDic[inputString[i]] += 1
    else:
        inputDic[inputString[i]] = 1

maxKey = ''
maxValue = 0
for i in range(len(inputDic)):
    if inputDic[inputDic.keys()[i]] > maxValue :
        maxKey = inputDic.keys()[i]
        maxValue = inputDic[inputDic.keys()[i]]
        
if maxKey.isalpha() and maxKey.islower():
    if inputDic.get(maxKey.upper()) == maxValue :
        maxKey = maxKey.upper()

print maxKey,maxValue