"""
import threading
import time  #delay, calcualation


function:
    Thread :main function for thread initialization
    start: to start the thread
    join:  this function will check for thread completation

why thread required:

"""
"""
import time
def squre(n):
    print("This is the function use to find squre :")
    for i in n:
        print("Squre of {0} is ".format(i),i*i)
        time.sleep(0.5)

def cube(n):
    print("This is the function use to find cube :")
    for i in n:
        print("Cube of {0} is :".format(i),i*i*i)
        time.sleep(.02)
t=time.time()
a=[1,2,3,4,5,6]
squre(a)
cube(a)
print("Time taken by system is :",time.time()-t)
"""



import time
import threading as ti
def squre(n):
    print("This is the function use to find squre :")
    for i in n:
        print("Squre of {0} is ".format(i),i*i)
        time.sleep(0.1)

def cube(n):
    print("This is the function use to find cube :")
    for i in n:
        print("Cube of {0} is :".format(i),i*i*i)
        time.sleep(0.1)
t=time.time()
a=[1,2,3,4,5,6]
t1=ti.Thread(target=squre,args=(a,))
t2=ti.Thread(target=cube,args=(a,))
t1.start()
t2.start()
t1.join()
t2.join()



print("Time taken by system is :",time.time()-t)








