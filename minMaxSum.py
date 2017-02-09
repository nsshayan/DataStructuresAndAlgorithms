#import sys

'''
Given a list of integers find the smallest possible sum and the largest possible sum.
'''

#a,b,c,d,e = raw_input().strip().split(' ')
#a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

nos = raw_input().strip().split(' ')

nos = map(int,nos)
nos.sort(cmp=None, key=None, reverse=False)

print sum(nos[:-1]),sum(nos[1:])

