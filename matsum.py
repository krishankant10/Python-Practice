n=int(input("Enter first matrix row"))
m=int(input("Enter first matrix column"))
a=[]
for i in range(n):
    a.append([])
    for j in range(m):
        k=int(input()) 
        a[i].append(k)

        
p=int(input("Enter Second matrix row :"))
q=int(input("Enter Second matrix column :"))

b=[]
for i in range(p):
    b.append([])
    for j in range(q):
        k=int(input()) 
        b[i].append(k)

print("First matrix is :",a)
print("second matrix is :",b)

if(p==n and m==q):
    c=[]
    for i in range(p):
        c.append([])
        for j in range(q):
            k=int(a[j][i])+int(b[j][i])
            c[i].append(k)

print("sum is :",c)
