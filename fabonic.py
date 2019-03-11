def fabonic(n):
    n1=0;
    n2=1;
    for i in range(0,n):
        print(n1,end=" ")
        nth=n1+n2;
        n1=n2;
        n2=nth;
        
a=int(input("Enter any number"))
    fabonic(a)
