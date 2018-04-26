# Uses python3
import sys

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
    for _ in range(1,remainder):
        res = (first + second)%m
        first = second 
        second = res
    return res%m
        
def get_fibonacci_pisano(n,m):
    period = get_pisano_period(m)
    print("Period: ",period)
    return (n%period)
   
if __name__ == '__main__':
    #input = sys.stdin.read();
    n, m = map(int, input().split())
    print(get_fibonacci_huge(n, m))