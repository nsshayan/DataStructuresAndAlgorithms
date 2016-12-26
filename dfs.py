'''
Unreachable nodes - we need to find the number of unreachable nodes in the graph. dfs can be used
to find the number of unreachable nodes
'''

N,M = raw_input().split(" ")

#initializing adjacency list
g= [[]for y in range(int(N))]

#creating the graph with edge from a to b
for i in range(int(M)):
    a,b=raw_input().split(" ")
    g[int(a)-1].append(int(b)-1)
    g[int(b)-1].append(int(a)-1)

#headNode
x = int(raw_input())

visited = [0 for y in range(int(N))]
def dfs(g,headNode):
    visited[headNode]=1
    for w in g[headNode]:
        if visited[w]==0:
            dfs(g,w)

dfs(g,x-1)    
#print visited
print visited.count(0)