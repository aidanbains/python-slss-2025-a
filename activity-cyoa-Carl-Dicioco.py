# Choose Your Own Adventure
# Carl Dicioco
# 24 September
#
# Choose your own adventure story focusing
# on using variables and branching/conditionals

import sys


greeting = "Welcome to the game."
print(greeting)
health = 100
inventory = []
user_name = input("Put your name down below.")
print(f"Welcome to the game, {user_name}.")
choice = input("Do you want to start the game now? (yes/no)").lower()

if choice == "yes":
    print("You wake up in a dark hallway.")
    print("The floor is cold, and the walls are cracked and dirty.")
    print("Dim lights flicker above you.")
    print("You see broken hospital signs on the walls.")
    print("The place looks abandoned and silent.")
    print("You see three things around you:")
    print("1. a lighter")
    print("2. a key")
    print("3. a roll of bandages")
elif choice == "no":
    print("You did not start the game. Play again?")
    sys.exit()
else:
    print("Invalid answer.")

choice1 = input("Which object do you take? (lighter/key/bandages)").lower()

if choice1 == "lighter":
    inventory.append("lighter")
    print("You picked up a lighter. It can be useful for seeing things better.")
elif choice1 == "key":
    inventory.append("key")
    print("You find an unfamiliar key. Its purpose is a mystery to you.")
elif choice1 == "sword":
    inventory.append("bandages")
    print("You pick up a roll of bandages. These might come in handy later.")
else:
    print("You ignored everything and walked forward.")


print("You continue walking down the hallway.")
print("Suddenly, you hear something shatter in a room near you.")
