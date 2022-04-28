import random

gene=input("Enter genes in binary representation: ")
mutation_prob=float(input("Enter mutation probability: "))

str=""

for i in range(len(gene)):
    random_prob=random.random()
    if random_prob>mutation_prob:
        str+="1"
    else:
        str+="0"
for i in range(len(gene)):
    if str[i]=="1":
        if gene[i]=="1":
            gene=gene[:i]+"0"+gene[i+1:]
        else:
            gene=gene[:i]+"1"+gene[i+1:]

print("Probability string: ",str)
print("Mutated gene in binary representation: ",gene)