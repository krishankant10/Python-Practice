'''
Exception Handling

types:
Zero  Division Error
Type Error
Nmae erroe
IO Error
Attribute Error
value error
etc etc etc

syntax:
    the code which can produce an error
except typeofexception:
    write the message or report we have to give
finally:
    write the code which should exect if exception occor or not
'''
'''
try:
    a=int(input("Enter a number"))
except ValueError:
    print("Please enter only integer value")
finally:
    print("program terminated")
print("bhibhfbshb")
'''
'''
try:
    a=int(input("Enter a number"))
except:
    print("ohh! something want wrong")
finally:
    print("program terminated")
'''
'''
try:
    a=int(input("Enter a number"))
    b=int(input("Enter b number"))
    c=a/b
    print("Divide of a/b is :"+c)
except ZeroDivisionError:
    print("Divide by zero")
finally:
    print("program terminated")
'''
'''
#User defined Exception
class ExptForce(Exception):
    pass
try:
    a=int(input("Enter any number"))
    b=int(input("Enter any number"))
    if(b==0):
        raise ExptForce
except ExptForce:
    print("Why you are entering value zero")
        
'''

task:
    projects insert exception handling
    mysql data transeferring
    tic tak tok
    gui integrate database
    web scrapping: excel(links)

advise: make dynamic codes always.
