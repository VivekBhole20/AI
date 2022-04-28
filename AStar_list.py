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
        
        if n==target or n not in adjList:
            pass
        else:
            for m in adjList[n]:
                w=m[1]
                if m[0] not in open_set and m[0] not in closed_set:
                    open_set.add(m[0])
                    parents[m[0]]=n
                    g[m[0]]=g[n]+w
                
                else:
                    if g[m[0]]>g[n]+w:
                        g[m[0]]=g[n]+w
                        parents[m[0]]=n
                        
                        if m[0] in close_set:
                            open_set.add(m[0])
                            closed_set(m[0])
        if n==target:
            path=[]
            while parents[n]!=n:
                path.append(n)
                n=parents[n]
            path.append(src)
            path.reverse()
            
            print("Path Exists!!!\n")
            print(g[target])
            
            return path
        
        open_set.remove(n)
        closed_set.add(n)
    
    print("Path does Not Exists!!!\n")
    return -1

adjList={0:[(1,2),(2,4)],1:[(3,2),(4,1)],2:[(5,3),(6,2)]}

src=0
target=6

path=AStarAlgo(src,target)

print(path,'\n')