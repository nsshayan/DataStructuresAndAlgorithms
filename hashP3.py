import string
import Queue
import operator

characters = list(string.lowercase[:])

charQueue = Queue.Queue()

characters.insert(0, '1')

characters.remove('1')
 
print characters

T = int(raw_input())

for i in range(T):
    inputString = raw_input()
    inputDic = {}
    for j in range(len(inputString)):
        if inputString[i] in characters:
            characters.remove(inputString[i])
        if inputDic.has_key(inputString[i]):
            inputDic[i] += 1
        else :
            inputDic[i] = 1
    
    