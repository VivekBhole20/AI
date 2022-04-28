import numpy as np

size=7

def Hill_Climbing(src,target):
    i=src
    min=100
    
    while i!=target:
        temp_i=i
        print("\nCurrent Node: ",i," , ",min)
        print("Edges\n")
        for j in range(size):
            if adjMatrix[i][j]!=0:
                print(j," , ",adjMatrix[i][j])
                if adjMatrix[i][j]<min:
                    min=adjMatrix[i][j]
                    temp_i=j;
        if temp_i!=i:
            i=temp_i
        else:
            break
    
    if i==target:
        print("\nCurrent Node: ",i," , ",min)
    else:
        print("\nTarget node not found")

adjMatrix=np.zeros((size,size),dtype=int)

edges={(0,1,2),(0,2,4),(1,3,2),(1,4,1),(2,5,3),(2,6,2)}

for edge in edges:
    adjMatrix[edge[0]][edge[1]]=edge[2]

src=0
target=4

#print(adjMatrix)
Hill_Climbing(src,target)