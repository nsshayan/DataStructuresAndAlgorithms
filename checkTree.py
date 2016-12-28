'''
Given :-
the number of nodes in a graph
the degree of each of the vertices

Find whether the given graph is tree or not
'''

N = int(raw_input())

Degree = raw_input().split(" ")

sum = 0

for i in range(len(Degree)):
    sum = sum + int(Degree[i])

if sum/2 == N-1:
    print "YES"
else :
    print "NO"