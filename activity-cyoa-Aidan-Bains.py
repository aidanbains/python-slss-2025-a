# Choose Your OWn Adventure
# Aidan Bains
# 24 September

# Choos Your Own Adventure story focusing on using
# variable and branching/conditionals

# Intro
from tkinter.constants import YES


greeting = "Hello! Welcome to my game!"
print(greeting)
user_name = input("What is your name?")
print(f"Nice to meet you{user_name}")
game = input("Would you like to start the game now?")

if game == "yes":
    print("OK, let's begin the game")
    print("You have landed at Tilted Towers and you need to get ready for battle.")
    print("What do you want to do first.")
    print("1.Search for loot")
    print("2.Get Material for building.")

choice1 = input("Enter 1 or 2:")

if choice1 == "1":
    print("You open chests around you and get a sword and sheild.")
    print(" You are now ready for war.")
elif choice1 == "2":
    print("You pickaxe trees for wood")
    print("You are ready for survival")
else:
    print("Invalid choice. You wasted time and got sniped.")
    print("GAME OVER")

print("The storm is coming. You have to move to the circle to be safe.")
print("Do you:")
print("1. Rush to circle and look for fights.")
print("2. Hide in a bush and wait.")

choice_storm = input("Enter 1 or 2:")

if choice_storm == "1":
    print("You push into the circle and spot an enemy")
    print("You build up quickly and win the fight, but lose some health.")
elif choice_storm == "2":
    print("You stay hidden in a bush. Nobody sees you, but you miss a supply drop.")
else:
    print("You hesitated and the storm eliminated you.")
    print("GAME OVER")

print("You see a supply drop nearby.")
print("Do you:")
print("1. Open the supply drop.")
print("2. Ignore it and stay safe.")

choice_drop = input("Enter 1 or 2:")

if choice_drop == "1":
    print("You open the supply drop and get a rocket launcher!")
elif choice_drop == "2":
    print("You play it safe, but someone else gets the supply drop.")
else:
    print("You couldn't decide and got ambushed.")
    print("GAME OVER")

print("Congrats you have made it to the final two players")
print("Have two options first go and battle the last player or go into a heal off")

choice2 = input("Enter 1 or 2:")

if choice2 == "1":
    print("Good choice!")
    print("You find the last player")
    print(
        "You build up for high ground they try to knock you down but you jump on them and take them out"
    )
    print("Well done")
    print("#1 VICTORY ROYALE")
elif choice2 == "2":
    print("Playing it safe. Smart choice.")


elif game == "no":
    print("GAME OVER")


# Problem


# Rising Action

# Climax

# Resolution
