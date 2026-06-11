def main():
    x=int(input("Enter a value: "))
    if isEven(x):
        print("The value is even")
    else:
        print("The value is odd")

def isEven(n):
    if n%2==0:
        return True
    else:
        return False

main()
    