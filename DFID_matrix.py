import numpy as np

def DLS(src,target,maxDepth,path):
    print("-----Next Iteration-----")
    print("Current Node: ",src)
    path.append(src)
    print("Path: ",path)
    
    if src==target:
        return True
     
    elif maxDepth<=0:
        return False
    
    for i in range(7):
        if adjMatrix[src][i]!=0:
            if DLS(i,target,maxDepth-1,path):
                return True
    
    return False

def DFID(src,target,maxDepth):
    for i in range(maxDepth):
        path=[]
        if DLS(src,target,i,path):
            return True
    return False

#change the no of nodes as per your graph
size=7

adjMatrix=np.zeros((size,size),dtype=int)

#Write your edges in the format (source node,destination node) for every edge;
edges={(0,1),(0,2),(1,3),(1,4),(1,5),(1,6)}


for edge in edges:
    adjMatrix[edge[0]][edge[1]]=1;

src=0
target=5
maxDepth=3

if DFID(src,target,maxDepth):
    print("The target is reachable from the source\n")
else:
    print("The target is NOT reachable from the source\n")