# game.py
print("Welcome to my Rock-Paper-Scissors game...")
print(f'USER_NAME')


import random

#print(10)
#print(10, 99, "My message", "another message")
user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")
#print("USER CHOICE:")
print("Rock, Paper, Scissors, Shoot!")
#print(user_choice)
print("USER CHOICE: ", user_choice)
# validate the input such that only if it is one of the expected values
# ... will we continue with the rest of the program
# ... otherwise we'll stop the progam before it tries to do anything else
# ... and we'll ask the user to run the program again
# and
# or
# this is variable assignment using a single =
#x = 5
# this is equality checking with a double ==
# "is this equal to that?"
#
#if user_choice = "rock" or "paer" or "scissors": # THIS LINE IS PSEUDOCODE
# if user_choice == "rock":
if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit()
#print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")










valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(["rock","paper","scissors"])
print("COMPUTER CHOICE: ", computer_choice)

#this is the if statement to simulate the event where rock beats scissor
if (user_choice == "rock" and computer_choice == "scissors"):
    print("Flawless Victory! Good Job!")
elif (user_choice == "scissors" and computer_choice == "rock"):
    print("Mhmm Computer wins..its okay...Try again!")

#this is the if statement to simulate Paper beating Rock
if (user_choice == "paper" and computer_choice == "rock"):
    print("Flawless Victory! Good Job!")
elif (user_choice == "rock" and computer_choice == "paper"):
    print("Mhmm Computer wins..its okay...Try again!")

#this is to simulate scissors beating paper
if (user_choice == "scissors" and computer_choice == "paper"):
    print("Flawless Victory! Good Job!")
elif (user_choice == "paper" and computer_choice == "scissors"):
    print("Mhmm Computer wins..its okay...Try again!")


#this is the if statement to simulate a tie game
if (user_choice == computer_choice):
    print("Tie Game! Try Again")

print("THIS IS THE END OF OUR GAME. PLEASE COME AGAIN.")
