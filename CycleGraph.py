'''
Given the adjacency matrix 

Find the number of cycles of degree 4
'''

import numpy as np
import math

N = int(raw_input())

adjMat = []

for i in range(N):
    adjMat.append(map(int,raw_input().rstrip().split(" ")))
                  
#print N
#print adjMat
x = np.matrix(adjMat)

degree = 0
for i in range(N):
    degree = degree + math.pow(adjMat.count(1), 2)

print (np.trace(x * x * x * x) - degree)
