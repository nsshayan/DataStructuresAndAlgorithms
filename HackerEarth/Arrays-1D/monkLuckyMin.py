T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    nos = map(int,raw_input().strip().split())
    minNo = min(nos)
    if nos.count(minNo)%2 == 0:
        print 'Unlucky'
    else :
        print 'Lucky'