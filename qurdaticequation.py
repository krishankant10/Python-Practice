import  cmath
a = int(input("Enter the  value of A"))
b = int(input("Enter the  value of B"))
c = int(input("Enter the  value of C"))


''' Discriminent'''
d = (b**2) - (4*a*c)
root1 = (-b -cmath.sqrt(d)) / (2 * a)
root2 = (-b + cmath.sqrt(d)) / (2 * a)
print(root1)
print(root2)
