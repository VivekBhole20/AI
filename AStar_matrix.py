import numpy as np

heuristic=[10,5,7,4,3,1,0]

def AStarAlgo(src,target):
    open_set=set([src])
    closed_set=set()
    g={}
    parents={}
    
    g[src]=0
    parents[src]=src
    
    while len(open_set)>0:
        n=-1
        for v in open_set:
            if n==-1 or g[n]+heuristic[n]>g[v]+heuristic[v]:
                n=v
        
        if n==target or np.all(adjMatrix[n]==0):
            pass
        
        else:
            for m in range(size):
                if adjMatrix[n][m]!=0:
                    w=adjMatrix[n][m]
                    
                    if m not in open_set and m not in closed_set:
                        open_set.add(m)
                        g[m]=g[n]+w
                        parents[m]=n;
                    else:
                        if g[n]+w<g[m]:
                            g[m]=g[n]+w
                            parents[m]=n
                            
                            if m in closed_set:
                                open_set.add(m)
                                closed_set.remove(m)
        
        if n==target:
            path=[]
            while parents[n]!=n:
                path.append(n)
                n=parents[n]
            path.append(src)
            path.reverse()
            
            print("Path Exists!!!\n")
            print(g[target],"\n")
            return path
        
        closed_set.add(n)
        open_set.remove(n)
    
    print("Path does NOT Exists!!!\n")
    return -1
            

size=7

adjMatrix=np.zeros((size,size),dtype=int)

edges={(0,1,2),(0,2,4),(1,3,2),(1,4,1),(2,5,3),(2,6,2)}

for edge in edges:
    adjMatrix[edge[0]][edge[1]]=edge[2]

src=0
target=6

#print(adjMatrix)
path=AStarAlgo(src,target)
print(path,"\n")