"""Given an array of n integers(duplicates allowed). 
Print “Yes” if it is a set of contiguous integers else print “No”.
https://practice.geeksforgeeks.org/problems/check-if-array-contains-contiguous-integers-with-duplicates-allowed/0
"""

T = int(input())

def isContiguousArray(a):
    for i in range(len(a)-2):
        if a[i+1]==a[i]+1:
            continue
        else:
            return "No"
    return "Yes"
 
#a.sort(key=None, reverse=False)
for i in range(T):
    
    n = int(input())
    a = list(map(int,input().strip().split()))
    print(isContiguousArray(list(set(sorted(a)))))
    
    