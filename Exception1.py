try:
    a=int(input("Enter any number"))
    b=int(input("Enter any number"))
    if(b==0):
        raise
    else:
        print(a/b)
except Exception:
    print("error")
finally:
    print("Program terminated")
