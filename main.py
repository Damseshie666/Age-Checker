#Your task is to create a simple age checker for a roller coaster ride in python.
"""The program should ask the user to enter their age. Based on their age, provide different messages.
1) If the user is between 18 & 45 years old (inclusive), print "Enjoy the ride!"
2) If the user is under 18 years old, print "You're too young for this ride"
3) If the user is over 45 years old, print"You're too old for this ride"
"""

print ("To get access to the roller coaster ride")
user_age = input("How old are you?")
user_age = int(user_age)

if user_age >= 18 and  user_age <= 45:
    print("Enjoy the ride!")
elif user_age < 18 :
    print("You're too young")
elif user_age > 45 :
    print("You're too old")
