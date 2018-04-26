T = int(raw_input())
F =[0,1]
def fibo(N):
    for i in range(len(N)-1,N+1):
        F.append(F[i-1]+F[i])
    return F[N]
for i in range(T):
    N = int(raw_input())
    if N == 1:
        print F[N]
    elif len(F) < N:
        print fibo(N) 
    else:
        print F(N) 