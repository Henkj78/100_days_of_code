import random

print("Let's play Rock, Paper or Scissors!\n")

player_choice = input("Player, you're up! Enter 'Rock', 'Paper' or 'Scissors': ").lower()

# Rock wins against scissors
# scissors wins against paper
# paper wins against rock

# Let computer choose
computers_choice = random.randint(0, 3)
if computers_choice == 0:
    computers_choice = "rock"
elif computers_choice == 1:
    computers_choice = "paper"
else:
    computers_choice = "scissors"

# print what player chose
print(f"\nYou chose {player_choice}")

# print what computer chose
print(f"The computer chose {computers_choice}\n")

# Write code and print who won
if player_choice == "rock" and computers_choice == "scissors":
    print("You won!")
elif computers_choice == "rock" and player_choice == "scissors":
    print("The computer won!")
elif player_choice == "scissors" and computers_choice == "paper":
    print("You won!")
elif computers_choice == "scissors" and player_choice == "paper":
    print("The computer won!")
elif player_choice == "paper" and computers_choice == "rock":
    print("You won!")
elif computers_choice == "paper" and player_choice == "rock":
    print("The computer won!")
elif player_choice == computers_choice:
    print("It's a tie!")
else:
    print("Something went wrong!")




