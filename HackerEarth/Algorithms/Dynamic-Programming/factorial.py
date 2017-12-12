# Write your code here
T = int(raw_input())
fact = [-1] * 100005
fact[0]=1
fact[1]=1

for i in range(2,len(fact)):
    fact[i] = i * fact[i-1]% (1000000000+7) 

def factorial(n):
    if fact[n]!=-1:
        return fact[n]
    fact[n]=n * factorial(n-1)
    if (n >  1000000000+7):
        return fact[n]%(1000000000+7)
    else:
        return fact[n]
    
for i in range(T):
    N = int(raw_input())
    print fact[N]
