def main():
    number=get_no()
    meow(number)

def get_no():
    while True:
        n=int(input("What's n? "))
        if n>0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()