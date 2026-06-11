name =input("What is your name: ")

match name:

 case "Kartikeya" | "Ansh" | "Mohan":
    print("Japanese Club")

 case "L"|"Light":
    print("Chess Club")

 case _:
    print("Unknown Club")