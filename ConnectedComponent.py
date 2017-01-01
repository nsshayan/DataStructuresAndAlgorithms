N,M = raw_input().split(" ")

g= [[]for y in range(int(N))]

for i in range(int(M)):
    a,b=raw_input().split(" ")
    g[int(a)-1].append(int(b)-1)
    g[int(b)-1].append(int(a)-1)
    
print g
visited = [0 for y in range((int(N)))]

def dfs(g,node,edges):
    visited[node] = 1
    for w in g[node]:
        if visited[w] == 0:           
            edges += dfs(g,w,edges)
        else :
            edges = 1 
    return edges
edgeList = []

for i in range(int(N)):
    edges = 0
    if visited[i]==0:
        edgeList.append(dfs(g,i,edges))

#print edgeList
print max(edgeList)