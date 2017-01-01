import operator
N,M,k = raw_input().split(" ")

val = raw_input().split(" ")

g= [[]for y in range(int(N))]

for i in range(int(M)):
    a,b=raw_input().split(" ")
    g[int(a)-1].append(int(b)-1)
    g[int(b)-1].append(int(a)-1)
    


for i in range(int(N)):
        #===========================================================================
    # if L < SL:
    #     temp = L
    #     L = SL
    #     SL = temp
    #     ele = g[i][0]
    #===========================================================================
    valNode = []
    for w in g[i]:
        valNode.append((int(val[w]),w))
        
    valNode.sort(key=operator.itemgetter(0), reverse=1)
    
    if len(valNode) < int(k):
        print -1
    else :
        #print valNode
        print valNode[int(k)-1][1]+1
          
             
 #key=operator.itemgetter(0),       
