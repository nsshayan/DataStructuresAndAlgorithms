T = int(raw_input())
for i in range(T):
    N,initial =  raw_input().strip().split()
    currHold = initial
    prevHold = initial
    for i in range(int(N)):
        testInput = raw_input().strip().split()
    
        if testInput[0]=='P':
            prevHold = currHold
            currHold = testInput[1]
        else:
            currHold,prevHold=prevHold,currHold
        
    print 'Player ' + currHold
        