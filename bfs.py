import Queue
N = raw_input() # Number of nodes

g = [[]for y in range(int(N))]

for i in range(int(N)-1):
    A,B = raw_input().split(" ")
    g[int(A)-1].append(int(B)-1)
    g[int(B)-1].append(int(A)-1)
    
level = raw_input()

#print N
#print int(N)-1
#print level
#print g

q = Queue.Queue()
visited = [0 for y in range(int(N))]
nodeLevel = [-1 for y in range(int(N))]

def bfs(g,rootNode):
        q.put(rootNode)
        visited[rootNode]=1
        #level = 0
        nodeLevel[rootNode]=0
        while (not q.empty()):
            vertex = q.get()
            #print g[vertex]
            for w in g[vertex]:
                #print w                
                if visited[w] == 0:
                    q.put(w)
                    visited[w]=1
                    nodeLevel[w]=nodeLevel[vertex]+1
        #print nodeLevel          
        print nodeLevel.count(int(level)-1)
            
bfs(g,0)
