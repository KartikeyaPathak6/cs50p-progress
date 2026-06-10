name = input("Hello, what is your name? ")
name = name.strip().title()

print(f"Hello, {name}! Wassup!")

age = int(input("What is your age? "))

print(f"Your age is {age}")

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

i = int(input("How many times do you want to repeat? "))

for x in range(i):
    print("hello world")