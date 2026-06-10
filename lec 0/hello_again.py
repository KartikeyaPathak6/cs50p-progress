def hello(to="baby"):
    print("hello,",to)

hello()
name =input("What is your name? ").strip().title()
hello(name)