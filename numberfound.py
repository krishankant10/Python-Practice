import re
"""
ob=re.compile(r'\d\d-\d{10}')
result=ob.search("Hello this is 91-9829320362.91-9784030765")
print("No found in string is",result.group())
"""
link='vdfygg@jnhjib,bvgjdfbvgjh@hbfhg,guydfgy@jbfdgbh'
ob=re.findall(r'[\w\.]+@+[\w\.]+',link)
for i in ob:
    print(i)
