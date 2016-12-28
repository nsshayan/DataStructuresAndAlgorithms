'''
Given:
Edges between nodes

Find the number of nodes

Testcase Sample
T # Number of testcases
E # Number of edges 
a b # Edge between node a and b
'''
from sets import Set

T = int(raw_input())


for i in range(T):
    E = int(raw_input())
    nodes = Set()
    for i in range(E):
        a,b = raw_input().split(" ")
        nodes.add(a)
        nodes.add(b)
    print len(nodes)
