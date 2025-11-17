# Question 1
age = int(input("How old are you right now?"))
print("In 2049, you will be", age + 31)


# Question 2

# Judges score
score1 = float(input("Judge 1: "))
score2 = float(input("Judge 2: "))
score3 = float(input("Judge 3: "))
score4 = float(input("Judge 4: "))
score5 = float(input("Judge 5: "))

# Calculate
average = (score1 + score2 + score3 + score4 + score5) / 5

# Final Average
avg = round(average, 1)
print(f"Your Olympic score is {avg}")

# Question 3

burger = input("Would you like a burger for $5? (Yes/No) ")
fries = input("Would you like fries for $3? (Yes/No) ")

total = 0

# Add burger if yes
if burger == "yes":
    total += 5

# Add fries if yes
if fries == "yes":
    total += 3

# Add 14% tax
total = total * 1.14

# Total
print("Your total is $", round(total, 2))
