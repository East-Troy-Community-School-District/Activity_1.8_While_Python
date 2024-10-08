# Magic 8 Ball
# Pawelski
# 10/7/2024
# Programming Fundamentals

import random

repeat = "y"
while repeat == "y":
    question = input("What would you like to ask? >> ")
    response = random.randint(1, 20)
    if response == 1:
        print("As I see it, yes.")
    elif response == 2:
        print("Ask again later.")
    elif response == 3:
        print("Better not tell you now.")
    elif response == 4:
        print("Cannot predict now.")
    elif response == 5:
        print("Concentrate and ask again.")
    elif response == 6:
        print("Don’t count on it.")
    elif response == 7:
        print("It is certain.")
    elif response == 8:
        print("It is decidedly so.")
    elif response == 9:
        print("Most likely.")
    elif response == 10:
        print("My reply is no.")
    elif response == 11:
        print("My sources say no.")
    elif response == 12:
        print("Outlook not so good.")
    elif response == 13:
        print("Outlook good.")
    elif response == 14:
        print("Reply hazy, try again.")
    elif response == 15:
        print("Signs point to yes.")
    elif response == 16:
        print("Very doubtful.")
    elif response == 17:
        print("Without a doubt.")
    elif response == 18:
        print("Yes.")
    elif response == 19:
        print("Yes – definitely.")
    elif response == 20:
        print("You may rely on it.")
    repeat = input("Would you like to ask another question? (y/n) >> ")
