a=int(input("Enter any number to check prime or not"))
k=0
for i in range (2,a):
    if(a%i==0):
        k=1
if(k==1):
    print("not prime")
else:
    print("Given number is prime")
