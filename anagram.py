import math
T = int(raw_input())

def factoradic(S,k,index):
    n = len(S)
    nb = math.factorial(n) // math.factorial(n-k)
    if index >= nb:
        raise IndexError
    res = []
    while k > 0:
        nb = nb // n
        pos = index // nb   # the factoradic digits
        index = index % nb      # the remaining digits
        res.append(S[pos])
        del S[pos]
        k = k-1
        n = n-1
    return res

        

for i in range(T):
    S,N = raw_input().strip().split()
    N = int(N)
    print S,N
    S = list(sorted(S))
    print str(factoradic(S,len(S),N))

# import itertools
# T = int(raw_input())
# 
# 
# for i in range(T):
#     S,N = raw_input().strip().split()
#     N = int(N)
#     anagrams = ["".join(arrangement) for arrangement in itertools.permutations(S)]
#     anagrams.sort(cmp=None, key=None, reverse=False)
#     
#     print anagrams[N-1]
