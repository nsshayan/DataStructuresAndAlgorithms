t = int(input()) #number of testcases
for i in range(t):
    nos = int(input())
    n = list(map(int,input().strip().split())) # numbers
    dict_n = dict((k,1) for k in n) #dictionary of numbers
    no_q = int(input()) # number of queries
    for j in range(no_q):
        q = list(map(int,input().strip().split()))
        if len(q) == 1:
            if q[0] in dict_n:
                print('Yes')
            else :
                print('No')
        elif len(q)==no_q:
            for k in q:
                if k in dict_n:
                    print('Yes')
                else:
                    print('No')
            break
        
