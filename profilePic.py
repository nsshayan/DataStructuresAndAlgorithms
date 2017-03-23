# Profile Picture (HE)

L = int(raw_input())
N = int(raw_input())
for i in range(N):
    W,H = map(int,raw_input().strip().split(' '))
    if W < L or H < L :
        print 'UPLOAD ANOTHER'
    elif W== L and H == L :
        print 'ACCEPTED'
    else :
        print 'CROP IT'