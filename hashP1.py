'''
Given a String P. Can the string P be divided into two strings A and B such that A + B = P and A = B
Characters can be removed from the string to create the required string 

wow  # o is removed to form the string P
Yes 
'''
T = int(raw_input())

for i in range(T):
    alphabets = [0 for i in range(26)]
    testcase = raw_input()
    for j in range(len(testcase)):
        alphabets[ord(testcase[j])-97] += 1
    
    success = 0
    for k in range(len(alphabets)):
        if alphabets[k] > 1 :
            print 'Yes'
            success = 1
            break
    if success == 0:
        print 'No'
        
