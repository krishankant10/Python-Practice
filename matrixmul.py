row1=int(input("How Many Rows in First Matrix :"))
col1=int(input("How Many Column in First Matrix :"))
X=[]
for i in range(row1):
    X.append([])
    for j in range(col1):
        k=int(input("Enter ({0},{1}) Element:".format(i,j)))
        X[i].append(k)

row2=int(input("How Many Rows in Second Matrix :"))
col2=int(input("How Many Rows in Second Matrix :"))
Y=[]
i=0
j=0
for i in range(row2):
    Y.append([])
    for j in range(col2):
        k=int(input("Enter ({0},{1}) Element:".format(i,j)))
        Y[i].append(k)

if(col1==row2):
    result=[]
    for i in range(row1):
        result.append([])
        for j in range(col2):
            k=int(0)
            Y[i].append(k)
    for i in range(row1):
       for j in range(col2):
           for k in range(row2):
               result[i][j] += X[i][k] * Y[k][j]
else:
    print("Multipication Not posible")

print("matrix multipication is:")
for r in result:
   print(r)
