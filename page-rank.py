import numpy 
graph={}
temp=[]
alpha=0.1
accuracy=10e-8
with open("tiny.txt") as file:
    N=int(file.readline())
    for i in file:
        for num in i:
            if num.isnumeric():
                temp.append(int(num))
for i in range(len(temp)//2):
    if temp[2*i] not in graph.keys():
        graph[temp[2*i]]=[temp[2*i+1]]
    else:
        graph[temp[2*i]].append(temp[2*i+1])
for key,val in graph.items():
    n=len(val)
    temp=[]
    for num,item in enumerate(set(val)):
        temp.append([item,alpha/n+(1-alpha)*val.count(item)/n])
    graph[key]=temp

matrix=[]
for i in range(N):
    matrix.append([])
    for j in range(N):
        if i in graph.keys():
            matrix[i].append(0)
    for j in graph[i]:
        matrix[i][j[0]]=j[1]
matrix=numpy.matrix(matrix)
x=[1/N for i in range(1,N+1)]
x=numpy.array(x)
x_temp=numpy.matmul(x,matrix)

while(True):
    matrix_temp=matrix
    good=0
    # print(x,x_temp)
    for i,elem in enumerate(x_temp):
        # print(x_temp.take(i),x.take(i),"|||")
        if (abs(x_temp.take(i)-x.take(i)))<accuracy:
            
            good+=1
    if good==len(x):
        print(x_temp)
        break
    # matrix=numpy.matmul(matrix,matrix_temp)
    x=x_temp
    x_temp=numpy.dot(x_temp,matrix)
    # print(x_temp,matrix)
    print(x,x_temp,"||||||")

