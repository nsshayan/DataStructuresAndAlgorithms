N = int(raw_input())

A = map(int,raw_input().strip().split())

X = [-2]*N
Y = [-2]*N
stk = []
stk.append(N-1)
for prev in range(N-2,-1,-1):
    while len(stk)!=0:
        if A[stk[len(stk)-1]]<A[prev]:
            X[stk.pop()]=prev+1
        else :
            break
    stk.append(prev)

while len(stk)!=0:
    X[stk.pop()]=-1
    
stk.append(0)

for nex in range(1,N):
    while len(stk)!=0:
        if A[stk[len(stk)-1]] < A[nex]:
            Y[stk.pop()]=nex+1
        else:
            break
    stk.append(nex)
    
while len(stk)!=0:
    Y[stk.pop()]=-1
    
list3 = [(x + y) for x, y in zip(X, Y)]

#print X,Y
#print str(list3)
print ' '.join(map(str, list3))
