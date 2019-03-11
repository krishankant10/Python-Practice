def prime(a):
    for i in range(2,a):
        k=0
        for j in range(2,i):
            if(i%j==0):
                k=1
        if(k==0):
            print(i,end=" ")
n=int(input("Enter any number to print between prime numbers"))
prime(n)
