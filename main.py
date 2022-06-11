import random

print("Welcome to Rock, Paper, Scissors")
print("R represents Rock")
print("P represents Paper")
print("S represents Scissors")


possible_choices = ["R", "P", "S"]

while True:
    player_choice = input("Pick a choice from R, P, S: ")
    player_choice = player_choice.upper().strip()
    
    if player_choice not in possible_choices:
        print("Invalid choice, pick either R, P or S ")
        continue
    
    computer_choice = random.choice(possible_choices)
    print(f"Player ({player_choice}) :  CPU ({computer_choice})")
    
    if player_choice == "R" and computer_choice == "s":
       print("You win!")

    elif player_choice == "P" and computer_choice == "R":
        print("You win!")

    elif player_choice == "S" and computer_choice == "P":
        print("You win!")

    elif player_choice == computer_choice:
        print("It's a tie, try again")
        continue

    else:
        print("Computer wins!")
    break    
    


