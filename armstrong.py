a=int(input("Enter any number:-"))
k=a
b=0
s=0

while a:
    b=a%10
    s+=b**3
    a=int(a/10)
if(k==s):
    print("it is armstrong")
else:
    print("it is not armstrong")
