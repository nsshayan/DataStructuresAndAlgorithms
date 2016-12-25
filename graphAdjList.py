N,M = raw_input().split(" ")

g = [[]for y in range(int(N))]

for i in range(int(M)):
    A,B = raw_input().split(" ")
    g[int(A)-1].append(int(B)-1)
    
Q = raw_input()

for i in range(int(Q)):
    A,B = raw_input().split(" ")
    if (int(B)-1) in g[int(A)-1]:
        print "YES"
    else :
        print "NO"