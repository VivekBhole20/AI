size=7

def DFSUtil(src,target,visited,path):
    visited.add(src)
    path.append(src)
    if src==target:
        print(path)
        print("Target Found!!!")
        return False
        
    if src in adjList:
        for i in adjList[src]:
            if i not in visited:
                DFSUtil(i,target,visited,path)

def DFS(src,target):
    connected=True
    visited=set()
    path=[]
    print("Path: ")
    while connected:
        connected=DFSUtil(src,target,visited,path)

adjList={0:[1,2],1:[3,4],2:[5,6]}

src=0
target=5

DFS(src,target)