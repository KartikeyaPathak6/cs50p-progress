from calculator import square

def main():
    x=int(input("Enter a number:"))
    print(test_square(x))
    
def test_square():
    for n in (2, 3, -2, 0, 10):
        assert square(n) == n * n

if __name__ =="__main__":
    main()