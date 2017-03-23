T = int(raw_input())


for k in range(T):
    N,X = map(int,raw_input().split(' '))
    C = map(int,raw_input().split(' '))
    C.sort()
    count = 1
    S = 0
    for i in range(2,len(C)):
        S += C[i]
        if S > X:
            break
        count += 1
    print count
