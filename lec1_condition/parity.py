def main():
    x=int(input("Enter a value: "))
    if isEven(x):
        print("The value is even")
    else:
        print("The value is odd")

def isEven(n):
    return n%2==0

main()
    