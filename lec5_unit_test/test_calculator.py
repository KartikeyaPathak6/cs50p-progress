from calculator import square

def main():
    x=int(input("Enter a number:"))
    print(test_square(x))

def test_square(n):
    if square(n) != n * n:
        return "it did not square"
    else:
        return square(n)

if __name__ =="__main__":
    main()