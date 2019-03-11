
class snake:
    name='python'
    def charname(self,nwname):
        self.name=nwname

s=snake()
print(s.name)
s.charname("anaconda")
print(s.name)
'''
'''
class snake:
    def __init__(self,name):
        self.name=name
s=snake('python')
a=snake('anaconda')
print(s.name)
print(a.name)
'''
'''
class snake:
    name='python'
    def charname(self,name):
        self.name=name
        return 10,20
s=snake()
x,y=s.charname('anaconda')
print(s.name)
print(x,y)
'''
'''

principle

inheritence

'''

'''
class polygon:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def param(self):
        return self.a+self.b+self.c
class triangle(polygon):
    def __init__(self,x,y,z):
        polygon.__init__(self,x,y,z)

t=triangle(10,20,30)
res=t.param()
print(res)


#private __


class cls:
    def prin(self,name=None):
        if(name==None):
            print("User not valid")
        else:
            print("Welcome sir! ",name)
c=cls()
c.prin()
c.prin("Chaman")
