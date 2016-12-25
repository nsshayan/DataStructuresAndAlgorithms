N,M = raw_input().split(" ")


g = [[0 for x in range(int(N))] for y in range(int(N))]
#for i in range()
#print M,N
#print g

for i in range(int(M)):
    A,B = raw_input().split(" ")
    g[int(A)-1][int(B)-1] = g[int(B)-1][int(A)-1]= 1

#print g
Q = raw_input()

for i in range(int(Q)):
    A,B = raw_input().split(" ")
    if g[int(A)-1][int(B)-1] == 1:
        print "YES"
    else :
        print "NO"