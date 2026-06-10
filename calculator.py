def add(x, y):
    return x + y

def divide(x, y):
    return round(x / y, 2)

def square(n):
    return pow(n, 2)

x = float(input("What's x? "))
y = float(input("What's y? "))
z = float(input("what's square z? "))

print("Divide",divide(x, y))
print("Add",add(x,y))
print("Square",square(z))