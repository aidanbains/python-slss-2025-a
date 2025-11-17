# Numbers and Operations
# Author: Aidan Bains
# 5 November

# Work with numbers and operations


# Create an algorithm to gather data to find the most popular bubble tea plaace around us

# Show all the choices
# Keep track

# Version 1
def vote_listed_choices():
    """Display all choices
    5 users votes fro their choices
    Results will be printed"""
    CHOICES = [
        "A. Blenz",
        "B. Bubble Queen",
        "C. Sun Tea",
        "D. heytea",
        "E. CoCo",
        "F. Fresh T",
    ]

    Blenz = 0
    Bubble_Queen = 0
    Sun_Tea = 0
    heytea = 0
    CoCo = 0
    Fresh_T = 0

    # Show all the choices
    print("Vote for your favourite from the list.")
    print("Give the letter of your choice.")
    for choice in CHOICES:
        print(choice)
    # Ask the user for their choice
    vote = input("Your Vote").strip(",.!?")
    # Keep track of a tally
    if vote == "A":
        Blenz = Blenz + 1
    elif vote == "B":
        Bubble_Queen += 1
    elif vote == "C":
        Sun_Tea += 1
    elif vote == "D":
        heytea += 1
    elif vote == "E":
        CoCo += 1
    elif vote == "F":
        Fresh_T += 1

    # Data analysis


# Version 2
# Ask the user to give their favourite bubble tea place
# Keep track of a tally
# Data analysis
# Give the raw percentage score
# Give scores as a precentage


def main():
    vote_listed_choices()


if __name__ == "__main__":
    main()
