from collections import Counter
import operator
T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    R = map(int,raw_input().strip().split())
    A = map(int,raw_input().strip().split())
    A = Counter(A)
    R = Counter(R)
    ha = sorted(A.iteritems(), key=operator.itemgetter(1,0),reverse=True)[0][0]
    hr = sorted(R.iteritems(), key=operator.itemgetter(1,0),reverse=True)[0][0]
    #hr = sorted(R, key=lambda k: (-R[k], k), reverse=True)[0]

    #ha = sorted(A.items(), key=operator.itemgetter(1),reverse=True)[0][0]
    #hr = sorted(R.items(), key=operator.itemgetter(1),reverse=True)[0][0]
    #print A,R
    print ha,hr
    if ha < hr:
        print 'Rupam'
    elif ha == hr:
        print 'Tie'
    else:
        print 'Ankit'