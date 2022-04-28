size=7

def UCS(src,target):
    queue=set([src])
    path=[]
    g={}
    
    g[src]=0
    
    while len(queue)>0:
        n=-1
        
        for v in queue:
            if n==-1 or g[n]>g[v]:
                n=v
        
        if n==target or n not in adjList:
            pass
        else:
            for i in adjList[n]:
                w=i[1]
                if i[0] not in queue:
                    queue.add(i[0])
                    g[i[0]]=g[n]+w
                else:
                    if g[i[0]]>g[n]+w:
                        g[i[0]]=g[n]+w
                
        if n==target:
            path.append(target)
            print("Path Exists!!!\n",path)
            print("\nCost: ",g[target])
            return
        queue.remove(n)
        path.append(n)
    
    print("\nPath does NOT Exists!!!")

adjList={0:[(1,2),(2,4)],1:[(3,2),(4,1)],2:[(5,3),(6,2)]}

src=0
target=5

UCS(src,target)