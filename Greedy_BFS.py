h=[10,5,7,4,3,1,0]

size=7

def GreedyBFS(src,target):
    open=set()
    closed=[]
    parents={}
    
    open.add(src)
    parents[src]=src
    
    while len(open)>0:
        n=-1
        
        for v in open:
            if n==-1 or h[v]<h[n]:
                n=v
        
        if n==target or n not in adjList:
            pass
        else:
            for v in adjList[n]:
                if v not in open and v not in closed:
                    open.add(v)
                    parents[v]=n
                else:
                    parents[v]=n
                    if v in closed:
                        closed.remove(v)
                        open.add(v)
        
        if n==target:
            path=[]
            closed.append(target)
            while parents[n]!=n:
                path.append(n)
                n=parents[n]
            path.append(src)
            path.reverse()
            
            print("Path Exists!!!\n")
            print("Closed: ",closed)
            
            return path
        closed.append(n)
        open.remove(n)
    
    print("path does not exists!!!\n")
    return -1

adjList={0:[1,2],1:[3,4],2:[5,6]}

src=0
target=6

path=GreedyBFS(src,target)

print(path)