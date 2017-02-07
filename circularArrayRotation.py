import collections

n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
def rotate(l,n):
    return l[n:] + l[:n]

a = map(int,raw_input().strip().split(' '))
a = collections.deque(a)
a.rotate(k)
for a0 in xrange(q):
    m = int(raw_input().strip())
    print a[m]


