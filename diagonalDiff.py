#    Diagonal Difference

#import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

p = 0
s = 0
for i in range(0,n):
    #print a[i][i]
    p += a[i][i]
    s += a[i][n-i-1]


print abs(p-s)
