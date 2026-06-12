def take():
    names = []
    x = int(input("No. of students: "))
    for i in range(x):
        names.append(input("Name of the student: ")) #used append here which adds names to the list
    return names

def give(names):
    for i in range(len(names)):
        print(i+1, names[i])

give(take())
