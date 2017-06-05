
N = int(raw_input())
nos = map(int,raw_input().strip().split())
odd = []
even = []
digit=[0]*10
sum  = 0
flag = 0
for i in range(N):
    if nos[i]%2==0:
        even.append(nos[i])
    else:
        odd.append(nos[i])
        
L = min(len(even),len(odd))
for i in range(N):
    if len(even) != 0 and len(odd) != 0:
        n1 = str(max(even))
        n2 = str(max(odd))
    else :
        break
    listN1 = [int(d) for d in str(n1)]
    listN2 = [int(d) for d in str(n2)]
    
    for n in listN1:
        if digit[n] == 1:
            even.remove(int(n1))  
            flag = 1         
            break
        else:
            continue
    if flag == 1:
        continue
    
    else:
        for j in listN1:
            digit[j]=1
    
    for m in listN2:
        if digit[m] == 1:
            odd.remove(int(n2))  
            flag = 1         
            break
        else:
            continue
    if flag == 1:
        for j in listN2:
            digit[j]=0
        continue
    else:
        for j in range(len(listN2)):
            digit[listN2[j]]=1
            
    sum += int(n1)+int(n2)      
    odd.remove(int(n2))
    even.remove(int(n1))
    flag = 0  
    

print sum
