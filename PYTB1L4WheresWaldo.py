import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)

index = people.index('Waldo')

for x in people:
    if x == "Waldo":
        break

print("Waldo zit op nummer",index,)

print(people)
