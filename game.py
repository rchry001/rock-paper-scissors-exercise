
# game.py

print("Rock, Paper, Scissors, Shoot!")


#print (10, 99, "My Message", "Another Message")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

#print (user_choice)


print("USER CHOICE", user_choice)

#validate the input such that only if it is one of the expected values
#...will we continue with the rest of the program

#if user_choice = "rock" or "paper" or "scissors":
#if user_choice == "rock":
if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("Valid. Keep Going")
else:
    print("Oops, invalid input. Please try again.")
    exit()

print("This is the end of our game. Please play again.")
