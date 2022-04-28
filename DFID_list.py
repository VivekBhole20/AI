import numpy as np

def DLS(src,target,maxDepth,path):
    print("-----Next Iteration-----")
    print("The current node is ",src)
    path.append(src)
    print("Path = ",path)
    
    if src==target:
        return True
    
    elif maxDepth<=0:
        return False
        
    for i in adjList[src]:
        if DLS(i,target,maxDepth-1,path):
            return True
            
    return False
    
def DFID(src,target,maxDepth):
    for i in range(maxDepth):
        path=[]
        if DLS(src,target,i,path):
            return True
    return False


adjList={0:[1,2],1:[3,4],2:[5,6]}

src=0
target=5
maxDepth=3

if DFID(src,target,maxDepth):
    print("The target is reachable from the source\n")
else:
    print("The target is NOT reachable from the source\n")