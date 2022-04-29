size=7

def BFS(src,target):
    visited=set()
    queue=[]
    queue.append(src)
    visited.add(src)
    
    while len(queue)>0:
        curr=queue.pop(0)
        print(curr,end=" , ")
        if curr==target:
            break
        
        if curr in adjList:
            for i in adjList[curr]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
    



adjList={0:[1,2],1:[3,4],2:[5,6]}

src=0
target=5

BFS(src,target)
print("\n")