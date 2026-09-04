def main():
    a=int(input("Enter a number: "))
    b=int(input("Enter another number:"))
    
    print("1.Add \n2.Multiply\n3.Divided\n4.Subtract\n")

    while True:
        try:
            cal=int(input("Select one: "))
            match cal:
                case 1:
                    print(a+b)
                case 2:
                    print(a*b) 
                case 3:
                    print(a/b) 
                case 4:
                    print(a-b)
            break
        except ValueError:
            print("Value was not an number(1-4)")
main()
