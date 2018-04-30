'''https://practice.geeksforgeeks.org/problems/ishaan-loves-chocolates/0'''

T = int(input())

for i in range(T):
    N = int(input())
    A = list(map(int,input().strip().split()))
    while len(A) != 1:
        if A[0]<A[len(A)-1]:
            A.pop(-1)
        else:
            A.pop(-len(A))
    
    print(A[0])
            