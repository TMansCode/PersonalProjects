
#Rock paper scissors game
import random
def Play_Game():
    #List out options that both the player and computer can choose from

    list = ['rock','paper', 'scissors']

    #player chooses an option

    player_choice = input('rock paper scissors\n')
    player_choice = player_choice.lower() 
    print("You chose, " + player_choice) 

    #computer chooses an options

    computer_choice = random.choice(list)
    print("Computer chose, " + computer_choice)

    #comparisons to see who won?
    #This will determine who wins based on the player's and computer's choice.

    if player_choice == 'rock':
        if computer_choice == 'paper':
            print('Paper covers rock, computer earns the win')
        elif computer_choice == 'scissors':
            print('Rock tops scissors, player earns the win')
        else:
            print('We have a tie, nobody wins')
    if player_choice == 'paper':
        if computer_choice == 'rock':
            print('Paper covers rock, player earns the win')
        elif computer_choice == 'scissors':
            print('Scissors cuts paper, computer earns the win')
        else:
            print('We have a tie, nobody wins')
    if player_choice == 'scissors':
        if computer_choice == 'rock':
            print('Rock tops scissors, computer earns the win')
        elif computer_choice == 'paper':
            print('Scissors cuts paper, player earns the win')
        else:
            print('We have a tie, nobody wins')
#This is where the game starts.
def main():
    Play_Game()
    ask = input("Would you like to play again? y/n")
#If user says yes, then keep playing
    if ask.lower() == 'yes':
        main()
    else:
        print("Well that's that, thank you for playing!")
main()