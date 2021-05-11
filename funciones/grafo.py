import random
d=2;
r1=1;
r2=4;

a=[[0 for x in range(d)] for y in range(d)]
for i in range (0,d):
    for j in range (0,d):
        print("Ingrese el valor",i,",",j)
        a[i][j]=int(input())
        #a[i][j]=int(random.randint(r1,r2))
        
print("Matriz A= ",a)

