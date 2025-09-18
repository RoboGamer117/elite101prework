import sys
choice = 0
print("Hello there! I am chatbot!")
name = input("What is your name?")
print(f"Hello {name}!")
age = input("How old are you?")
while True:
    try:
        year = int(age)
        if (year < 13):
            print("Wow you aren't even a teen yet! So young!")
        elif (year >= 13 and year <= 18):
            print("Oh you are just in your teens! Have fun in high school!")
        elif (year >= 19 and year <= 24):
            print("Wow you're probably in college! Must be interesting!")
        elif (year > 24):
            print("Wow I assume you are done with school. I hope you have fun at your j*b")
        break
    except ValueError:
        print("Please give a valid age")
        age = input("How old are you?")

def menu():
    print("1: Placeholder 1\n2: Palceholder 2\n3: Placeholder 3\n4: Exit the conversation")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        print("Placeholder 1")
    elif (choice == 2):
        print("Placehodler 2")
    elif (choice == 3):
        print("Placeholder 3")
    elif (choice == 4):
        sys.exit()

print("How can I help you today?")
while (choice != 4):
    menu()

