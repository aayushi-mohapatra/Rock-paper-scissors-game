import random
print("Rock, Paper, Scissors!")
while True:
    print("Enter your choice:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    
    choice = int(input("Enter your choice: "))
    while choice < 1 or choice > 3:
        choice = int(input("Invalid choice. Enter again: "))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print('Your choice:', choice_name)
    
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer's choice:", comp_choice_name)
    print(choice_name, "vs", comp_choice_name)

    if choice == comp_choice:
        print("It's a tie!")
    elif (choice == 1 and comp_choice == 3) or \
         (choice == 2 and comp_choice == 1) or \
         (choice == 3 and comp_choice == 2):
        print("You win!")
    else:
        print("Computer wins!")
    ans = input("Do you want to play again? (Y/N): ").lower()
    if ans == 'n':
        print("Game over")
        break
