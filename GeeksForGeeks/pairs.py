T = int(input())

for i in range(T):
    n = int(input())
    a = list(map(int,input().strip().split()))
    pairsList = []
    pairs =''
    for i in range(n):
        if (-1 * a[i]) in a and a[i] not in pairsList and (-1 * a[i]) not in pairsList:
            if a[i]<0:
                pairsList.append(-1 *a[i])
            else :
                pairsList.append(a[i])
        
    for i in range(len(sorted(pairsList))):
        pairs += '-'+str(pairsList[i])+' '+str(pairsList[i])+' '
    
    print (pairs)
    

