def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

a=int(input("Enter any Number:-"))
b=fact(a)
print(b)
