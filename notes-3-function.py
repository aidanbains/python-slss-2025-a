# functions
# Author: Aidan Bains
# 8 October

# function to print "Hello"
def say_hello():
    print("hello")


say_hello()


# function to print  personallized hello
def say_hello_nicely(name: str):
    print(f"hello{name}!")


def normalize_input():
    """Takes user input and cleans it up."""
    output = input().lower().strip(",.?! ")
    return output


# ask the user what the weather is
weather_reply = normalize_input()
print(weather_reply)
