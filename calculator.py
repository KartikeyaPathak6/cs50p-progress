def add():
    x= float(input("What's x?"))
    y= float(input("what's y?"))
    
    z= round(x/y,2)
    
    print(z)

def square(n):
    n=int(input("Enter a number"))
    return pow(n, 2)

square(add())
