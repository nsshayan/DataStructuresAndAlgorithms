T = int(raw_input())
for i in range(T):
    testCase = raw_input()
    if testCase == testCase[::-1]:
        if len(testCase)%2 == 0:
            print 'YES EVEN'
        else :
            print 'YES ODD'
    else :
        print 'NO'