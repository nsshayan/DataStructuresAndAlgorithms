# Uses python3
import sys
from pandas.core.indexes import period

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%m

    return current % m

def get_pisano_period(m):
    
    first = 0
    last = 1
    current = first+last
    
    for period in range(0,m*m):
        current = (first+last)%m
        first = last 
        last = current
        if first == 0 and last == 1:
            return (period + 1) 

def get_fibonacci_huge(n,m):
    remainder = n % get_pisano_period(m)
    first = 0 
    second = 1
    res = remainder
    sum = first + second
    for _ in range(1,remainder):
        res = (first + second)%m
        sum = (sum + res)%m
        first = second 
        second = res
        
    return sum%m
        
def get_fibonacci_pisano(n,m):
    period = get_pisano_period(m)
    print("Period: ",period)
    return (n%period)

def get_sum(m,period):
    F0 = 0
    F1 = 1
    if period == 0:
        total = 0
    else :
        total = F0+F1
    for _ in range(2,period+1):
        F2 = (F1 + F0)%m
        total = (total + F2)%m
        F0= F1 
        F1 = F2
    return total%m    
   
if __name__ == '__main__':
    #input = sys.stdin.read();
    n = int(input())  
    period = get_pisano_period(10)
    #print("period :",period)
    sum_per_period = get_sum(10,period)
    #print("sum per period:",sum_per_period)
    if n < period :
        totalSum = get_sum(10,n)
    else :        
        q = n/period
        r = n%period
        sum_q_periods = (q * sum_per_period)%10
        remaining_sum = get_sum(10,r)
        totalSum = sum_q_periods + remaining_sum
        #print("remaining sum:",remaining_sum)
    
    print(int(totalSum%10))
    #n, m = map(int, input().split())
    #print(get_fibonacci_huge(n, 10))